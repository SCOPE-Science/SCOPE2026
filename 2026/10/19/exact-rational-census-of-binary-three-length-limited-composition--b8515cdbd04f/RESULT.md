# Exact rational census of binary three-length-limited composition profiles

## Finding

For a binary word \(w\in\{0,1\}^n\), let \(C_{\leq3}(w)\) be the multiset of compositions (counts of zeros and ones) of **all contiguous nonempty substrings of lengths one, two, or three**. Every occurrence is counted, and the order of symbols within a substring is forgotten. For each positive integer \(n\), let \(R_3(n)\) be the number of different multisets \(C_{\leq3}(w)\) arising from words of length \(n\).

Then the ordinary generating function is precisely
\[
\boxed{\sum_{n\geq1}R_3(n)z^n
=\frac{z(2-5z+6z^2-4z^3+4z^4-z^5+2z^6-3z^7+2z^8)}{(1-z)^5(1+z)(1+z^2)}.}
\]
In explicit form, \(R_3(1)=2\), and for every \(n\geq2\),
\[
\boxed{R_3(n)=\frac{3n^4-16n^3+114n^2-272n+\kappa_n}{96},\qquad
\kappa_n=\begin{cases}480,&n\equiv0\pmod4,\\456,&n\equiv2\pmod4,\\555,&n\text{ odd}.\end{cases}}
\]
In particular the exact count is a degree-four quasipolynomial with period four after the first length, and
\[
\boxed{R_3(n)=\frac{n^4}{32}+O(n^3).}
\]
The first values, for \(n=1,\ldots,16\), are
\[
2,3,6,10,20,35,62,101,160,241,354,502,696,941,1250,1629.
\]
A fixed-length code whose distinct codewords have distinct \(C_{\leq3}\)-observations has maximum size exactly \(R_3(n)\), because one can choose exactly one word from each observation class.

## Assumptions and scope

The alphabet is binary, positions are a linear string rather than a circle, and **multiplicity** of each observed composition is retained. For a substring of length \(j\), the composition is the number of ones together with the known length \(j\). If \(n<3\), absent longer substrings contribute zero. This is the fixed-length, length-at-most-three observation model, not the full substring-composition model and not ordered adjacent-factor observation.

Write \(Z\) and \(K\) for the total zero and one counts. For each \(a\in\{0,1\}\), write \(R_a\) for the number of maximal \(a\)-runs, \(S_a\) for the number of those runs having length one, and \(L_a=R_a-S_a\) for the number of runs of length at least two. These run variables are used only for nonconstant words. Let \(e\) be the number of endpoint runs that are either long zero-runs or singleton one-runs; there are two distinct endpoint runs for every nonconstant word.

## Proof

**1. A complete run-and-boundary signature.** For a nonconstant word, the length-two observation records \(Z-R_0\) copies of \(00\) and \(K-R_1\) copies of \(11\), as every run of length \(h\) contributes \(h-1\) adjacent equal pairs. At length three, the numbers of all-zero and all-one triples are respectively
\[
Z-2R_0+S_0,\qquad K-2R_1+S_1.
\]
Indeed, a run of length \(h\) contributes \(\max(0,h-2)\) homogeneous triples, equal to \(h-2+\mathbf 1_{h=1}\). Thus the observations determine \(Z,K,R_0,R_1,S_0,S_1\).

A triple with exactly one one is of type \(001,010,100\). Each long zero-run contributes a candidate at each run end bordering a one, and each singleton one-run contributes one \(010\) if it is not an endpoint run. Correcting for the endpoint exceptions gives
\[
T_1=2L_0+S_1-e.
\]
Thus \(e=2L_0+S_1-T_1\) is itself observed. Conversely, the number of triples with two ones is
\[
T_2=2L_1+S_0-(2-e),
\]
and the other length-three counts are the two homogeneous ones already given. The length-one and length-two remaining counts follow from their lengthwise totals. Therefore two nonconstant words have identical \(C_{\leq3}\) observations **if and only if** their tuples \((Z,K,R_0,R_1,S_0,S_1,e)\) agree. Each constant word has its own observation and supplies one additional class.

**2. Feasibility of run lengths.** Given \(r\geq1\) runs of one symbol, exactly \(s\in\{0,\ldots,r\}\) of which are singletons, the set of realizable total lengths has generating function
\[
F_{r,s}(z)=
\begin{cases}
z^r,&s=r,\\
\displaystyle\frac{z^{2r-s}}{1-z},&0\leq s<r.
\end{cases}
\]
For \(s<r\), each nonsingleton run has length at least two, and any further excess length can be assigned to one of them. Hence these are *existence* generating functions: each feasible total length appears once, regardless of the number of words realizing it.

A nonconstant binary word alternates its zero-runs and one-runs, so necessarily \(|R_0-R_1|\leq1\); every such pair with feasible positive symbol lengths is possible.

**3. Distinct endpoint signatures.** When \(R_0=R_1=r\), the endpoints have opposite symbols. A zero-run endpoint can contribute zero or one to \(e\), with both possibilities available precisely when \(0<S_0<r\). Similarly, a one-run endpoint has both choices precisely when \(0<S_1<r\). The possible sums form an unbroken interval, of size
\[
1+\mathbf1_{0<S_0<r}+\mathbf1_{0<S_1<r}.
\]
When \(R_0=r+1\) and \(R_1=r\), the endpoints are both zero-runs. With \(R=r+1\geq2\) and \(s=S_0\), the possible numbers of long endpoint zero-runs have cardinality
\[
h_R(s)=1+\mathbf1_{1\leq s\leq R-2}+\mathbf1_{2\leq s\leq R-1}.
\]
The same count holds with the symbols exchanged (the complementary endpoint statistic then replaces \(e\)). These counts are realizable because assigning the specified singleton statuses to endpoints and interior runs and then assigning feasible positive lengths gives an actual word.

**4. Generating functions.** Let
\[
d=(1-z)^2,\quad
A_r=\sum_{s=0}^r F_{r,s}(z)=\frac{(1-z+z^2)z^r-z^{2r+1}}d,
\]
\[
B_r=\sum_{s=1}^{r-1}F_{r,s}(z)=\frac{z^{r+1}-z^{2r}}d,
\]
and, for \(R\geq2\),
\[
H_R=\sum_{s=0}^R h_R(s)F_{R,s}(z)
=\frac{(1+2z^2)z^R-(1+z+z^2)z^{2R-1}}d.
\]
The \(A_r^2\) term counts balanced run numbers with one baseline endpoint signature; the extra \(2A_rB_r\) counts the additional endpoint choices. The two imbalanced orientations together contribute \(2H_{r+1}A_r\). The two constant words contribute \(2z/(1-z)\). Therefore, as a formal power series,
\[
\sum_{n\geq1}R_3(n)z^n
=\frac{2z}{1-z}+\sum_{r\geq1}
\bigl(A_r^2+2A_rB_r+2H_{r+1}A_r\bigr).
\]
Each summand is a linear combination of geometric series in powers \(z^{2r},z^{3r},z^{4r}\). Using \(\sum_{r\geq1}z^{jr}=z^j/(1-z^j)\) for \(j=2,3,4\), putting terms over a common denominator, and cancelling factors yields exactly the displayed rational generating function. This is an identity of formal power series; no asymptotic or finite-data extrapolation is used.

Finally, the numerator without its leading factor of \(z\) evaluates to \(3\) at \(z=1\), while \((1+z)(1+z^2)=4\) there. The unique pole of order five is at \(z=1\); the other poles lie at \(-1\) and \(\pm i\) and have smaller orders. Coefficient extraction therefore gives leading term \(\frac34\binom{n+4}{4}=n^4/32+O(n^3)\). Partial fractions at fourth roots of unity give the displayed explicit residue-class formula for every \(n\geq2\), while the polynomial quotient of the generating function supplies the exceptional coefficient at \(n=1\).

## Verification

The standalone standard-library program `verify.py` checks three logically distinct finite routes. Literal word enumeration through length \(16\) constructs every substring-composition multiset and confirms its exact equivalence with the run-and-endpoint tuple. A separate finite run-feasibility enumeration counts signatures through length \(20\). A dynamic program that appends bits and retains only the last two symbols plus observable counts computes the distinct observations through length \(38\). Each independently agrees with the coefficient recurrence of the rational generating function.

Execute `python verify.py`; successful output begins `VERIFY_OK direct=1..16 structural=1..20 dynamic=1..38`. These computations test the proof but do not substitute for the all-length derivation.

## Relationship to prior work

Ye and Elishco introduced the length-limited substring-composition multiset and gave constructions for the model, including a treatment where the length limit scales with source length; they explicitly discuss fixed-limit capacity questions. Their results do not specify the number of observation classes when the length limit is three. Acharya and collaborators treat the **full** spectrum of substring compositions, which observes many more lengths and does not determine this quotient.

A publicly indexed exact result for the limit-two binary observation gives a quadratic enumeration and corresponding reconstruction classes. It does not state or imply the present limit-three quartic generating function: singleton-run statuses and endpoint effects arise from homogeneous and mixed triples unavailable at limit two. Nor does an adjacent-pair **ordered** spectrum, which distinguishes \(01\) from \(10\), imply this unordered three-length profile count. The same mathematical object is essential to the comparison, not merely similar terminology.

## Limitations

Only noiseless binary linear words with all substring compositions of lengths at most three, retaining multiplicities, are covered. The formula does not determine profile fibers individually, a minimum-redundancy encoding or fast ranking algorithm, higher length limits, nonbinary alphabets, or robustness to missing masses. Absence of a match in the searched literature cannot exclude an unpublished or differently indexed equivalent formula. No independent validation is claimed.

## References

1. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, first posted 31 August 2022, arXiv:2208.14963v1, https://arxiv.org/abs/2208.14963. See Section VIII and the conclusion (current open version v2).
2. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439, https://arxiv.org/abs/1403.2439; SIAM Journal on Discrete Mathematics 29 (2015).
3. *Exact binary \(r=2\) length-limited composition reconstruction*, publicly indexed research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-r-2-length-limited-composition-reconstruction--a98561a7f27e.
