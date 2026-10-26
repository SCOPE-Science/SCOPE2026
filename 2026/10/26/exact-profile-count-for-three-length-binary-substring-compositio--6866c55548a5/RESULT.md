# Exact profile count for three-length binary substring compositions

## Finding
Let \(\Sigma=\{0,1\}\). For every \(n\ge1\), a length-\(n\) word yields the multiset \(C_{\le3}(w)\) of compositions of **all contiguous substrings of lengths one, two, and three** (only those lengths not exceeding \(n\)); compositions retain the number of ones but forget their order. Let \(R_3(n)\) be the number of distinct such observations as \(w\) runs over \(\Sigma^n\). This equals the largest cardinality of a length-\(n\) zero-error reconstruction code for these observations.

The exact ordinary generating function is
\[
\sum_{n\ge1}R_3(n)z^n
=\frac{z(2-5z+6z^2-4z^3+4z^4-z^5+2z^6-3z^7+2z^8)}{(1-z)^4(1-z^4)}.
\]
For \(n\ge2\), equivalently,
\[
R_3(n)=\frac{3n^4-16n^3+114n^2-272n+c_{n\bmod4}}{96},
\qquad(c_0,c_1,c_2,c_3)=(480,555,456,555).
\]
The exceptional initial value is \(R_3(1)=2\). In particular, \(R_3(n)=n^4/32+O(n^3)\), so the exact maximum information content is \(4\log_2n-5+o(1)\) bits, despite the vanishing asymptotic rate.

## Assumptions and scope
Words are linear, not circular. Each occurrence of a substring contributes separately to the multiset, including overlapping occurrences. The observation identifies \(001\), \(010\), and \(100\) as the same length-three composition, and similarly identifies \(011\), \(101\), and \(110\). A zero-error code may choose arbitrary distinct words, but no two may give the same observation. Only the binary alphabet and the noiseless, fixed-length model are considered. The empty word is excluded.

## Proof
**Run invariants.** For a nonconstant word write \(p\) for its number of ones and \(z=n-p\) for its number of zeros. Let \(r_0,r_1\) be its numbers of runs of zeros and ones; let \(a_0,a_1\) count runs of the respective symbols of length exactly one. Thus \(t_i=r_i-a_i\) counts runs of length at least two. Let \(e_0\) be the number of zero endpoints (among the two end positions), and let \(s_i\) be the number of endpoints lying in singleton runs of symbol \(i\). The length-two composition multiplicities \(N_{00},N_{11}\) and length-three multiplicities \(N_{000},N_{111},N_1,N_2\) (where \(N_j\) has exactly \(j\) ones) are
\[
\begin{aligned}
N_{00}&=z-r_0,&N_{11}&=p-r_1,\\
N_{000}&=z-2r_0+a_0,&N_{111}&=p-2r_1+a_1,\\
N_1&=2r_0-2a_0-e_0+s_0+a_1-s_1,\\
N_2&=2r_1-2a_1-(2-e_0)+s_1+a_0-s_0.
\end{aligned}
\]
These follow by counting adjacent equal pairs in each run, pure triples in each run, and mixed triples crossing a run boundary. For example, \(001\) and \(100\) together occur \(2t_0\) times minus the long zero-runs at the two endpoints, while \(010\) occurs once for each interior singleton one-run.

Put \(\delta=r_0-r_1\) and \(\lambda=N_1-2r_0+2a_0-a_1=-e_0+s_0-s_1\). Necessarily \(\delta\in\{-1,0,1\}\) and \(\lambda\in\{-2,-1,0\}\). Conversely, the observation determines \(p,r_0,r_1,a_0,a_1,\lambda\): first retrieve \(p\) from singletons, then retrieve \(r_i\) from equal pairs, \(a_i\) from pure triples, and \(\lambda\) from \(N_1\). The displayed formulas reconstruct every other composition count, so these six integers describe exactly the observation classes.

**Feasible end conditions.** An endpoint contributes \(-1\) to \(\lambda\) if it is a long zero-run endpoint or a singleton one-run endpoint, and \(0\) otherwise. For nonconstant words the two endpoint runs are distinct. If \(\delta=1\), the word starts and ends in zero. The three values \(\lambda=0,-1,-2\) require, respectively, \(a_0\ge2\), \(a_0\ge1,t_0\ge1\), and \(t_0\ge2\). If \(\delta=-1\), both endpoints are one: the respective conditions are \(t_1\ge2\), \(a_1\ge1,t_1\ge1\), and \(a_1\ge2\). If \(\delta=0\), the endpoints differ: the respective conditions are \((a_0\ge1,t_1\ge1)\), \((t_0\ge1,t_1\ge1)\) **or** \((a_0\ge1,a_1\ge1)\), and \((t_0\ge1,a_1\ge1)\). In the middle case the intersection with all four parameters at least one must be subtracted once. All listed conditions suffice: arrange the alternating run types with the stipulated first and last statuses, distribute the designated singleton runs, and give every other run length two or more. Each long run accepts an arbitrary nonnegative number of additional symbols, independently.

**Count distinct observations, not words.** For integers \(A,T\ge0\), define the run-inventory series
\[
F_{A,T}(u,z)=\sum_{a\ge A,\ t\ge T}u^{a+t}\frac{z^{a+2t}}{(1-z)^{\mathbf1_{\{t\ge1\}}}}.
\]
The coefficient of \(u^r z^L\) is one exactly when a symbol has \(r\) runs, \(a\) singleton runs, \(t=r-a\) long runs, and total length \(L\) consistent with its minimum; here the summation over \(a,t\) regards these as independent signature coordinates rather than counting assignments of lengths to individual runs. Put \(V_0(z)=1-z+z^2\) and \(V_T(z)=z^T\) for \(T\ge1\). Geometric summation gives, for \(r\ge A+T\),
\[
[u^r]F_{A,T}(u,z)=\frac{V_T(z)z^r-z^{2r-A+1}}{(1-z)^2},
\]
and the coefficient vanishes for smaller \(r\).

Let \(H_d(A,T;B,U)\) be the generating function enumerating pairs of zero-run and one-run signatures with \(r_0-r_1=d\) and lower thresholds \(a_0\ge A,t_0\ge T,a_1\ge B,t_1\ge U\). Explicitly, \(H_d=[u^d]F_{A,T}(u,z)F_{B,U}(u^{-1},z)\), interpreted as the formal diagonal pairing of coefficients. Set \(m=\max(B+U,A+T-d,0)\). Multiplying the preceding two coefficient expressions and summing over \(r_1\ge m\) gives the exact rational identity
\[
H_d=\frac{1}{(1-z)^4}\left(
\frac{V_TV_Uz^{d+2m}}{1-z^2}
-\frac{V_Tz^{d-B+1+3m}+V_Uz^{2d-A+1+3m}}{1-z^3}
+\frac{z^{2d-A-B+2+4m}}{1-z^4}
\right).
\]
No infinite-word or asymptotic argument is used; these are four convergent formal geometric series.

The feasible-endpoint cases above give, writing the five arguments of \(H\) as \((d;A,T;B,U)\), exactly the following sum:
\[
\begin{aligned}
\sum_{n\ge1}R_3(n)z^n={}&\frac{2z}{1-z}\\
&+H_1(2,0;0,0)+H_1(1,1;0,0)+H_1(0,2;0,0)\\
&+H_{-1}(0,0;0,2)+H_{-1}(0,0;1,1)+H_{-1}(0,0;2,0)\\
&+H_0(1,0;0,1)+H_0(0,1;0,1)\\
&+H_0(1,0;1,0)-H_0(1,1;1,1)+H_0(0,1;1,0).
\end{aligned}
\]
The first term counts the two constant words at every positive length. Each remaining term enumerates distinct nonconstant signatures, not strings, with no duplication across distinct \(\delta,\lambda\) categories; the one subtraction is precisely the endpoint-condition intersection.

Substitute the rational identity for every \(H\), take the common denominator, and cancel \((1-z^2)(1-z^3)\). This gives the rational function stated under Finding. The supplied `verify_profiles.py` supplies a finite **integer-polynomial identity certificate** for precisely this cancellation (it does not infer an all-length theorem from a finite sample). Partial fraction expansion at the fourth roots of unity yields the displayed period-four quartic formula for \(n\ge2\), with \(R_3(1)=2\). Finally, a maximum code takes one representative of each observation class, proving its cardinality equals \(R_3(n)\).

## Verification
`verify_profiles.py` uses only the Python standard library. It reconstructs the rational-function simplification as an exact polynomial identity, checks the coefficient formula, exhaustively computes the literal profile of all binary words of lengths three through fourteen, cross-checks the run identities word by word, and independently enumerates profiles by a prefix-extension dynamic program through length thirty-five. The verifier prints `VERIFY_OK`. The exhaustive tests and dynamic program are corroboration only; the proof is the run-signature enumeration and the displayed all-length generating-function identity.

The first sixteen class counts are \(2,3,6,10,20,35,62,101,160,241,354,502,696,941,1250,1629\) for lengths one through sixteen.

## Relationship to prior work
Ye and Elishco introduced the length-limited substring-composition multiset model and studied reconstruction codes for a linear-length cutoff, explicitly identifying constant cutoffs and capacity bounds as open directions. This theorem gives an **exact**, not merely asymptotic, answer for the first cutoff beyond the two-letter case: the complete number of feasible observations for length at most three, with an explicit period-four law and a sharp quartic growth constant. A publicly available study of the binary cutoff two obtains a quadratic formula from run counts; it does not include length-three composition counts, where singleton-run statistics and additional endpoint statuses are indispensable. Ordered substring spectra retain strictly more information; counting their equivalence classes cannot be substituted for this result. The classical full substring-composition problem also observes longer factors and therefore does not imply this fixed-cutoff formula.

## Limitations
This is an exact count of observation classes and an existential optimal zero-error code cardinality. It does not construct an asymptotically efficient encoder/decoder for a canonical choice of representatives; it does not classify sizes of individual ambiguity classes; and it does not cover cutoff four or higher, larger alphabets, errors, missing readings, or cyclic strings. Literature retrieval is not a proof of novelty; unindexed equivalent counts remain a residual originality risk. No independent mathematical audit is claimed.

## References
1. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963v1, publicly posted 31 August 2022, especially Section VIII, https://arxiv.org/abs/2208.14963.
2. *Exact binary \(r=2\) length-limited composition reconstruction*, publicly available 2026 research note in the published-finding corpus mathematical findings repository; its theorem and proof concern the cutoff-two model only.
3. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, SIAM Journal on Discrete Mathematics 29 (2015), 1340–1371, DOI:10.1137/140962486.
