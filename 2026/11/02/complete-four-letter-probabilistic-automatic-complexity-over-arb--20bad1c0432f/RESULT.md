# Complete four-letter probabilistic automatic complexity over arbitrary finite alphabets

## Finding

Let \(\Sigma\) be any finite alphabet with \(|\Sigma|=q\ge 2\). Define \(A_P(w)\) as the smallest number of states in a probabilistic finite automaton for which \(w\) has strictly greater acceptance probability than every other word of the same length over \(\Sigma\). For every \(w\in\Sigma^4\),
\[
A_P(w)=\begin{cases}3,&w=abaa\text{ for distinct }a,b\in\Sigma,\\2,&\text{otherwise}.\end{cases}
\]
In particular, precisely \(q(q-1)\) of the \(q^4\) labeled four-letter words require three states. This is a complete classification simultaneously for every finite alphabet size \(q\ge2\).

## Assumptions and scope

A \(k\)-state probabilistic finite automaton has a row probability vector \(\pi\), row-stochastic transition matrices \(P_c\) indexed by \(c\in\Sigma\), and a zero-one accepting column vector \(\eta\). It assigns the word \(w=c_1\cdots c_n\) the score \(\rho(w)=\pi P_{c_1}\cdots P_{c_n}\eta\). A witness requires \(\rho(w)>\rho(z)\) for **every** distinct \(z\in\Sigma^n\). No fixed positive uniform gap across all lengths is required; the length here is exactly four. The hypothesis \(q\ge2\) avoids the degenerate unary-alphabet convention.

Two words have the same equality pattern when their positions have exactly the same equalities. Represent a pattern by its restricted-growth encoding, for example `0100` denotes \(abaa\), and `0123` denotes four pairwise distinct letters. There are exactly fifteen length-four patterns. Their classification is alphabet-independent once unused symbols are dealt with as below.

## Proof

A one-state stochastic automaton assigns the same probability (zero or one) to every word. Since \(q\ge2\), no word has complexity one.

**The exceptional pattern.** Kenneth Gill's binary two-state classification [1, Theorem 4.1; equivalent forms in Theorem 4.2] proves that `0100` cannot be uniquely maximized by a two-state probabilistic automaton over a two-letter alphabet. If a two-state automaton over a larger alphabet uniquely maximized \(abaa\), restricting its transition alphabet to \(\{a,b\}\) would give a forbidden binary witness. Hence \(A_P(abaa)>2\). The universal three-state construction of Kjos-Hanssen [2, Theorem 1.2] gives \(A_P(abaa)\le3\), proving equality.

**The other patterns.** For a word using \(s\ge2\) distinct letters, relabel them by first appearance as \(0,1,\dots,s-1\). Set \(\pi=(p,1-p)\), \(\eta=(1,0)^T\), and
\[
P_i=\begin{pmatrix}u_i&1-u_i\\v_i&1-v_i\end{pmatrix},\qquad
x_{t+1}=v_i+(u_i-v_i)x_t,\quad x_0=p.
\]
The explicit exact rational data \(p,(u_i),(v_i)\) in `CERTIFICATES.json` cover the thirteen nonconstant equality patterns other than `0100`. Every parameter belongs to \([0,1]\), so the matrices are stochastic. By enumerating the at most \(4^4=256\) active-alphabet words and evaluating the displayed affine recurrence in exact rational arithmetic, the certified minimum target-versus-competitor gaps are:

| Pattern | Number of active symbols | Exact strict gap |
|---|---:|---:|
| `0001` | 2 | \(3/16\) |
| `0010` | 2 | \(5/324\) |
| `0011` | 2 | \(119/8192\) |
| `0012` | 3 | \(3/128\) |
| `0101` | 2 | \(9/64\) |
| `0102` | 3 | \(12/625\) |
| `0110` | 2 | \(7/64\) |
| `0111` | 2 | \(9/64\) |
| `0112` | 3 | \(27/1024\) |
| `0120` | 3 | \(2/25\) |
| `0121` | 3 | \(1/8\) |
| `0122` | 3 | \(9/512\) |
| `0123` | 4 | \(35/4096\) |

These exact rational inequalities are a finite proof certificate, not an extrapolation. The scripts in `verify_fraction.py` and `verify_integer.py` independently evaluate all competitors by two arithmetic representations. In the constant case `0000`, start in accepting state zero, make the target letter act as identity and every other letter send both states to the rejecting state. This uniquely maximizes the constant word, using two states.

For a pattern using \(s\ge2\) symbols, extend its witness to any larger alphabet by assigning each unused symbol the average \(s^{-1}\sum_{i=0}^{s-1}P_i\) of the active transition matrices. A score of a word containing unused symbols becomes a convex average of scores of words using only active symbols; since at least one active replacement differs from the target and has positive mixture weight, this average is strictly below the target score. Thus extra symbols never introduce a tied maximum. Every nonexceptional length-four equality pattern consequently has a two-state witness over any permitted ambient alphabet.

Finally, exactly \(q(q-1)\) words have the exceptional form: choose the repeated symbol in \(q\) ways and the distinct second symbol in \(q-1\) ways. This proves the count.

## Verification

Run from this directory:

```sh
python3 verify_fraction.py
python3 verify_integer.py
```

Both require only the Python standard library. They read `CERTIFICATES.json`. The first uses exact `fractions.Fraction` calculations for all thirteen patterns, checks that the fifteen equality patterns are partitioned into the thirteen listed, the constant case, and the excluded `0100`, and checks a two-state constant-word witness. The second clears denominators independently and compares integer acceptance numerators, confirming the strict gaps. Recorded outputs are `FRACTION_OUTPUT.txt` and `INTEGER_OUTPUT.txt`.

## Relationship to prior work

Gill [1] completely classifies two-state probabilistic complexity on binary alphabets, and explicitly shows that binary `0100` requires more than two states. The binary portion of this theorem follows from that work; no novelty is claimed for it. Kjos-Hanssen [2] proves the universal upper bound of three states over every finite alphabet, which alone does not decide which multiletter words attain two. The contribution here is the complete **nonbinary** length-four classification, including all three- and four-distinct-letter patterns (notably `0123`), and its exact count for arbitrary alphabet size. The convex-mixture extension to unused symbols formalizes why small-alphabet certificates suffice.

## Limitations

The theorem only classifies words of length exactly four, over finite alphabets of at least two symbols. It does not classify the two-state probability-maximizer language at arbitrary lengths, nor bound the best possible acceptance gap. The positive cases use finite explicit rational witnesses; they do not yield a symbolic all-length construction. Publication priority beyond the inspected literature and searched research records is not independently established, and the review has not received an independent mathematical audit.

## References

[1] Kenneth Gill, *Probabilistic automatic complexity of finite strings*, arXiv:2402.13376, first posted 20 February 2024, especially §4 and Theorems 4.1–4.2. https://arxiv.org/abs/2402.13376

[2] Bjørn Kjos-Hanssen, *Every string has probabilistic automatic complexity at most three*, arXiv:2607.26275, first posted 28 July 2026, Theorem 1.2. https://arxiv.org/abs/2607.26275
