# Exact variance hierarchy for all binary four-symbol subsequence patterns

## Finding
Let \(W_n\) be a uniformly random length-\(n\) binary word, and for a fixed pattern \(p\in\{0,1\}^4\) let \(X_p(W_n)\) count ordered increasing quadruples of positions spelling \(p\). For all \(n\ge4\), the means are equal:
\[
\mathbb E[X_p]=\frac{1}{16}\binom n4.
\]
The exact second moment and variance, simultaneously for all sixteen patterns and every \(n\ge4\), are
\[
\mathbb E[X_p^2]=\sum_{t=4}^{8}c_t(p)2^{-t}\binom nt,\qquad
\operatorname{Var}(X_p)=\sum_{t=4}^{8}c_t(p)2^{-t}\binom nt-\frac1{256}\binom n4^2,
\]
where the following table gives all coefficients under reversal and bit complementation (each row covers its entire indicated symmetry orbit):

| Representative \(p\) | \(c_4\) | \(c_5\) | \(c_6\) | \(c_7\) | \(c_8\) | Orbit size |
|---|---:|---:|---:|---:|---:|---:|
| `0000` | 1 | 20 | 90 | 140 | 70 | 2 |
| `0001` | 1 | 14 | 60 | 110 | 70 | 4 |
| `0011` | 1 | 12 | 56 | 104 | 70 | 2 |
| `0010` | 1 | 10 | 44 | 94 | 70 | 4 |
| `0110` | 1 | 10 | 42 | 84 | 70 | 2 |
| `0101` | 1 | 8 | 36 | 80 | 70 | 2 |

Consequently the variances are **strictly ordered** in precisely that table order for every \(n\ge6\). At \(n=5\) only the rows `0010` and `0110` tie; at \(n=4\) all sixteen pattern variances equal \(15/256\). As \(n\to\infty\), the respective leading coefficients of \(n^7/645120\) are \(70,40,34,24,14,10\). In particular, the constant pattern has **seven times** the asymptotic variance of the alternating pattern although their means coincide.

## Assumptions and scope
The positions of \(W_n\) are independent fair bits. Occurrences are **scattered subsequences with multiplicity**: distinct index quadruples count separately even when their letters coincide. The order is for fixed four-letter patterns at every integer \(n\ge4\), not for contiguous-factor counts, distinct subsequence types, other pattern lengths, nonuniform sources, or arbitrary alphabet sizes. Reversal and complementation of both the pattern and the random source preserve the distribution, giving six orbits of sizes \(2,4,2,4,2,2\).

## Proof
For a four-element subset \(A=\{a_1<\cdots<a_4\}\) of \([n]\), write \(I_A(p)\) for the indicator that the bits at these positions equal \(p_1,\ldots,p_4\). Then \(X_p=\sum_A I_A(p)\), and \(\mathbb E I_A=2^{-4}\).

For each \(t\in\{4,5,6,7,8\}\), define the purely finite integer
\[
 c_t(p)=\sum_{\substack{A,B\subseteq[t],\ |A|=|B|=4\\ A\cup B=[t]}}
 \prod_{i\in A\cap B}\mathbf1\!\left[p_{\operatorname{rank}_{A}(i)}=p_{\operatorname{rank}_{B}(i)}\right].
\]
Here the sum runs over **ordered** pairs \((A,B)\), and \(\operatorname{rank}_A(i)\) is the rank of \(i\) inside the increasing list of \(A\). Each pair \((A,B)\) of four-position occurrences with union size \(t\) has \(\binom nt\) choices of union positions. If an intersection requires different symbols of \(p\) at the same text position, its joint probability is zero. Otherwise all \(t\) union bits are individually prescribed, so its joint probability is exactly \(2^{-t}\). Summing the probabilities proves the second-moment identity for every \(n\).

To evaluate the five finite coefficients, enumerate the pairs \((A,B)\) in the displayed definition. This is an exhaustive integer calculation over at most \(\binom84^2=4900\) pairs per pattern, not an extrapolation from word lengths. The accompanying standalone script evaluates the defining sum, independently checks its rows by full word enumeration, and certifies the table. Directly, \(c_4=1\) because \(A=B=[4]\), and \(c_8=\binom84=70\) because disjoint pairs are unconstrained. Reversal and bit complementation give the six table orbits; their sizes sum to sixteen.

The five coefficient columns are weakly decreasing from top to bottom, and each adjacent pair differs in at least one of \(c_5,c_6,c_7\). Therefore subtracting the common squared mean shows weak variance order for all \(n\ge4\), strict for \(n\ge6\) because \(\binom nt>0\) for all \(5\le t\le7\) then. At \(n=5\), the only adjacent equality arises from identical \(c_5=10\) for `0010` and `0110`. At \(n=4\), only the common \(c_4\) term survives, giving \(2^{-4}-(2^{-4})^2=15/256\). Finally, expanding the exact binomial formula yields the listed leading coefficients of \(n^7/645120\); the degree-eight terms cancel because disjoint position sets give independent indicators. This proves the sevenfold asymptotic ratio without assumptions about finite samples.

## Verification
Run `python3 verify_four_pattern_variances.py` with Python 3 standard library. The verifier recomputes all \(30\) entries \(c_t(p)\), checks the six disjoint reversal/complement classes, verifies coefficientwise order and its strictness conditions, and **independently enumerates every binary text of lengths \(4\) through \(11\)** to compare the exact first and second moments with the formula. Its observed output is `VERIFY_OK`. The infinite-length theorem follows from the subset-pair identity, not from the finite text census.

## Relationship to prior work
Menon and Singh (first public 13 June 2023) study the distribution of the number of occurrences of an arbitrary binary subsequence pattern and give small-occurrence enumerations, as well as maximum-occurrence results for patterns with at most three runs. Their paper gives the common mean but does not present the six-class exact variance hierarchy or the strict length-six transition. Janson and Szpankowski (2020) analyze random subsequence-pattern counts as generalized \(U\)-statistics and provide broader methods for asymptotic fluctuation analysis; these methods motivate exact moment study but the inspected text does not give this four-pattern comparative ordering. Earlier general moment treatments (Flajolet, Szpankowski and Vallée, 2006) make closed-form moment evaluation a known technique. The contribution here is the **complete exact comparative classification** and coefficientwise dominance, not the invention of a general second-moment method.

## Limitations
No priority or uniqueness claim is made against unindexed work: an already-evaluated variance table or equivalent pattern-comparison theorem could exist. The classification is specific to length-four patterns under independent fair binary letters. It says nothing about stochastic dominance of full pattern-count distributions, nor does a variance order imply a probability-tail order. The finite checker does not replace the all-length combinatorial identity.

## References
1. K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870v1 (first public 13 June 2023), https://arxiv.org/html/2306.07870v1.
2. S. Janson and W. Szpankowski, *Hidden Words Statistics for Large Patterns*, arXiv:2003.09584 (first public 21 March 2020), https://arxiv.org/abs/2003.09584; *Electronic Journal of Combinatorics* 28(2) (2021), P2.36.
3. P. Flajolet, W. Szpankowski, and B. Vallée, *Hidden word statistics*, *Journal of the ACM* 53(1) (2006), 147–183, https://doi.org/10.1145/1120582.1120586.
