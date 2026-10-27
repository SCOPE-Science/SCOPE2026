# A minimal ternary witness for two-state probabilistic automatic complexity

## Finding

Over the alphabet \(\Sigma=\{a,b,c\}\), the length-three word \(\mathtt{abc}\) has probabilistic automatic complexity \(A_P(\mathtt{abc},\Sigma)=2\). The rational two-state PFA with initial distribution \((1/3,2/3)\), accepting state \(A\), and letter updates \(p\mapsto 1/2+p/6\), \(p\mapsto 1/2-p/2\), and \(p\mapsto 1-2p/3\) for \(a,b,c\), respectively, gives \(\rho(\mathtt{abc})=47/54\) while every other length-three word has acceptance probability at most \(23/27\); the exact gap is \(1/54\).

## Assumptions and scope

A probabilistic finite automaton (PFA) has row-stochastic transition matrices, an initial probability row vector, and a fixed accepting-state indicator. Its acceptance probability is the probability of ending in an accepting state after reading the input. The alphabet is exactly \(\{a,b,c\}\), the initial distribution is \((1/3,2/3)\), and the second state \(A\) is the sole accepting state. All transition probabilities are rational and satisfy the ordinary PFA constraints. The result concerns length-three words and gives no classification for longer words or larger alphabets.

## Proof

Order the states as \((N,A)\), with \(N\) nonaccepting and \(A\) accepting. Use initial row vector \(\pi=(1/3,2/3)\) and accepting column vector \(\eta=(0,1)^T\). The transition matrices, with rows and columns ordered as \((N,A)\), are

\[
P_a=\begin{pmatrix}1/2&1/2\\1/3&2/3\end{pmatrix},\qquad
P_b=\begin{pmatrix}1/2&1/2\\1&0\end{pmatrix},\qquad
P_c=\begin{pmatrix}0&1\\2/3&1/3\end{pmatrix}.
\]

Each matrix is row-stochastic. If \(p\) is the current probability of state \(A\), reading a letter changes it to \(\alpha+(\beta-\alpha)p\), where \(\alpha\) is the transition probability from \(N\) to \(A\) and \(\beta\) is the transition probability from \(A\) to \(A\). Thus the three updates are \(f_a(p)=1/2+p/6\), \(f_b(p)=1/2-p/2\), and \(f_c(p)=1-2p/3\), starting from \(p_0=2/3\).

Exact rational iteration for every word of length three gives the following complete table. A row labels the first two letters; columns label the final letter.

| Prefix | Final \(a\) | Final \(b\) | Final \(c\) |
|---|---:|---:|---:|
| \(\mathtt{aa}\) | \(389/648\) | \(43/216\) | \(97/162\) |
| \(\mathtt{ab}\) | \(115/216\) | \(29/72\) | \(47/54\) |
| \(\mathtt{ac}\) | \(97/162\) | \(11/54\) | \(49/81\) |
| \(\mathtt{ba}\) | \(127/216\) | \(17/72\) | \(35/54\) |
| \(\mathtt{bb}\) | \(41/72\) | \(7/24\) | \(13/18\) |
| \(\mathtt{bc}\) | \(35/54\) | \(1/18\) | \(11/27\) |
| \(\mathtt{ca}\) | \(97/162\) | \(11/54\) | \(49/81\) |
| \(\mathtt{cb}\) | \(29/54\) | \(7/18\) | \(23/27\) |
| \(\mathtt{cc}\) | \(49/81\) | \(5/27\) | \(47/81\) |

The unique maximum is \(\rho(\mathtt{abc})=47/54\). The largest competing score is \(\rho(\mathtt{cbc})=23/27=46/54\), so the strict gap is \(47/54-23/27=1/54>0\). This verifies the two-state upper bound for \(A_P(\mathtt{abc},\Sigma)\).

A one-state PFA cannot distinguish inputs: its only transition matrix for each letter is the \(1\times1\) matrix \([1]\), and its acceptance indicator is constant. All words therefore have the same acceptance probability, so no one-state PFA has a unique most-likely length-three word. Hence \(A_P(\mathtt{abc},\Sigma)\ge2\), proving equality.

## Verification

The included standalone script `verify_pfa.py` uses exact rational arithmetic (`fractions.Fraction`) to check row-stochasticity, evaluate all \(3^3=27\) words, confirm the unique maximizer, and verify the exact gap. It prints `VERIFY_OK` after all assertions pass. The table above is the complete finite comparison, not a sample.

## Relationship to prior work

Gill classified the binary strings with \(A_P=2\) in Theorem 4.1 and proved in Corollary 4.18 that a binary string already having complexity two retains that property when the alphabet is enlarged [1]. Those statements do not classify a target that uses three distinct letters. Kjos-Hanssen proved \(A_P(w)\le3\) for every nonempty word over every finite alphabet and explicitly noted that the classification of strings with \(A_P=2\) over alphabets of size at least three was not carried out [2, Remark 5.3]. The present exact witness lies in that unresolved regime: it establishes a minimal three-symbol example, but not a general classification.

Targeted searches of public literature and paper text found no directly matching witness. The reviewed sources establish the binary classification and the universal three-state bound but do not state the displayed rational ternary witness. This bounded search does not establish absolute novelty.

## Limitations

This is a minimal boundary example, not a characterization of all words over three-letter alphabets. It does not determine \(A_P\) for longer words, establish computability for general alphabets, or quantify the best possible gap among two-state PFAs. The claim uses the standard model allowing arbitrary real transition probabilities; this witness happens to use rational probabilities.

## References

1. K. Gill, “Probabilistic automatic complexity of finite strings,” arXiv:2402.13376, first public version 2024-02-20; Theorem 4.1, Corollary 4.18, and Section 4.4.
2. B. Kjos-Hanssen, “Every string has probabilistic automatic complexity at most three,” arXiv:2607.26275, first public version 2026-07-28; Theorem 1.2, Corollary 5.2, and Remark 5.3.
