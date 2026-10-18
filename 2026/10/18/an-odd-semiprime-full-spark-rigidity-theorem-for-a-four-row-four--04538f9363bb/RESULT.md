# An odd-semiprime full-spark rigidity theorem for a four-row Fourier frame

## Finding
Fix any prime \(p\geq5\), set \(N=3p\), and select the four rows \(\mathcal R=\{0,1,2,5\}\) of the cyclic Fourier character matrix. For every four-element column set \(C\subset\mathbb Z/N\mathbb Z\), the corresponding minor is singular **if and only if** \(p=5\) and all four elements of \(C\) have the same residue modulo \(3\). In that exceptional case the minor has rank exactly three. Consequently the \(4\times N\) harmonic frame is full spark for every prime \(p\geq7\); at \(N=15\) precisely \(15\) of its \(\binom{15}{4}=1365\) maximal minors are singular, each obtained by deleting one point from one coset of the unique subgroup of order five.

This establishes sufficiency of the usual divisor-uniformity condition for this specific row pattern at every odd semiprime order \(3p\), despite the fact that divisor-uniformity alone is not sufficient for arbitrary composite cyclic Fourier patterns.

## Assumptions and scope
The matrix is \(F_N=(\xi^{rc})_{0\leq r,c<N}\), where \(\xi\) is any primitive \(N\)-th root of unity. A maximal minor uses the fixed set of four distinct row indices \(\mathcal R\), and an **unordered** set \(C\) of four distinct column indices. Changing \(\xi\) merely permutes columns, so the rank statements are independent of the primitive-root convention. Rank is over \(\mathbb C\). No claim is made for arbitrary four-row patterns, arbitrary composite orders, conditioning, or recovery in noise.

## Proof
**1. Reduce determinants to a ten-term root sum.** Write \(z_j=\xi^{c_j}\) for an ordering \(c_1,\ldots,c_4\) of \(C\). The generalized Vandermonde/Schur identity for the exponent pattern \(\{0,1,2,5\}\) gives
\[
\det(z_j^{r})_{r\in\mathcal R,\,1\le j\le4}
=\prod_{1\le i<j\le4}(z_j-z_i)\,h_2(z_1,z_2,z_3,z_4),
\qquad h_2=\sum_{1\le i\le j\le4}z_i z_j.
\]
Since the columns are distinct, the Vandermonde factor is nonzero. Thus singularity is equivalent to vanishing of the **ten-term** sum \(h_2\).

**2. Exact cyclotomic reduction.** Let \(\omega\) be a primitive third root and \(\zeta\) a primitive \(p\)-th root. Their product \(\omega\zeta\) is primitive of order \(3p\); we may use it for \(\xi\). For each \(a\in\{0,1,2\}\) and \(b\in\{0,\ldots,p-1\}\), let \(n_{a,b}\) be the number of pairs \(1\le i\le j\le4\) satisfying simultaneously
\[
c_i+c_j\equiv a\pmod3,\qquad c_i+c_j\equiv b\pmod p.
\]
Then \(h_2=\sum_{b=0}^{p-1}B_b\zeta^b\) where
\[
B_b=(n_{0,b}-n_{2,b})+(n_{1,b}-n_{2,b})\omega.
\]
Because the cyclotomic fields of orders \(3\) and \(p\) are linearly disjoint, the minimal polynomial of \(\zeta\) over \(\mathbb Q(\omega)\) is \(1+X+\cdots+X^{p-1}\). Therefore \(h_2=0\) **if and only if** all the \(B_b\) are equal. Linear independence of \(1,\omega\) over \(\mathbb Q\) then implies the existence of a fixed vector \(v=(v_0,v_1,v_2)\) of nonnegative integers with \(\min_a v_a=0\), and integers \(t_b\geq0\), such that
\[
(n_{0,b},n_{1,b},n_{2,b})=v+t_b(1,1,1)
\quad(0\leq b<p).
\]
Counting the ten pairs yields the **necessary and sufficient arithmetic equation**
\[
10=p(v_0+v_1+v_2)+3\sum_{b=0}^{p-1}t_b.
\tag{1}
\]

**3. An independent three-residue obstruction.** Let \(d_a\) be the number of column indices in \(C\) congruent to \(a\pmod3\), so \(d_0+d_1+d_2=4\). The counts of the ten pair sums in the three residues are
\[
H_0=\binom{d_0+1}{2}+d_1d_2,\qquad
H_1=\binom{d_2+1}{2}+d_0d_1,\qquad
H_2=\binom{d_1+1}{2}+d_0d_2.
\]
Evaluating the fifteen nonnegative solutions to \(d_0+d_1+d_2=4\), one obtains, up to a permutation of the three entries, **exactly**
\[
(H_0,H_1,H_2)\in\{(10,0,0),(6,3,1),(4,3,3)\}.
\tag{2}
\]
This is an elementary three-variable check, not an approximation.

**4. Exclude every prime except five.** For \(p\geq11\), equation (1) forces \(v_0+v_1+v_2=0\), after which it would require \(3\mid10\), an impossibility. For \(p=7\), equation (1) forces \(v_0+v_1+v_2=1\) and \(\sum_b t_b=1\). Consequently the three-residue pair-sum histogram is a permutation of \((8,1,1)\), excluded by (2). For \(p=5\), equation (1) forces \(v_0+v_1+v_2=2\) and \(\sum_b t_b=0\). The resulting histogram is a permutation of either \((10,0,0)\) or \((5,5,0)\); (2) excludes the latter. Hence every pair sum \(c_i+c_j\) has the same residue modulo three. Taking the difference of \(2c_i\) and \(c_i+c_j\) shows \(c_i\equiv c_j\pmod3\) for all \(i,j\).

**5. Attainment, count, and exact rank.** If \(p=5\) and \(C\) lies in one residue class modulo three, its four distinct members exhaust four of the five points in that class. Their fifth-root factors therefore form all fifth roots except one. For all five fifth roots \(w\), the generating identity \(\prod_{w^5=1}(1-wT)=1-T^5\) shows that, after omitting any one \(w_0\), the degree-two coefficient of \(\prod_{w\ne w_0}(1-wT)^{-1}=(1-w_0T)/(1-T^5)\) vanishes. Thus \(h_2=0\), proving the converse. There are \(3\binom54=15\) exceptional sets. Finally, the first three rows \(\{0,1,2\}\) form a full-rank \(3\times4\) Vandermonde submatrix on four distinct nodes, so every singular \(4\times4\) minor has rank **exactly three**. This completes all assertions.

## Verification
The standalone `CHECKER.py` constructs the cyclotomic coefficient arrays using only integer arithmetic. It exhaustively checks every four-column set for \(p=5,7,11,13\), respectively \(1365,5985,40920,82251\) sets, and obtains singular counts \(15,0,0,0\), with no mismatches against the theorem. It also independently enumerates all fifteen three-residue configurations and recovers exactly the histogram types in (2). The finite test is a reproducibility check; the proof above establishes the infinite-family statement.

Run from the extracted package directory using `python3 CHECKER.py` (standard library only). The accompanying `CHECKER_OUTPUT.txt` contains the recorded output.

## Relationship to prior work
Alexeev, Cahill and Mixon proved that divisor-uniformity characterizes full-spark harmonic row selections for **prime-power** Fourier orders, but showed that this condition is not generally sufficient for composite order. Here the modulus is the **squarefree** composite \(3p\), and the proof gives an exact additional sufficient condition for the fixed near-consecutive four-row pattern. Garcia, Karaali and Katz studied Fourier-minor nonvanishing and uncertainty principles; their general results do not count the present nonprincipal maximal minors. Malikiosis and Oussa describe broader algebraic full-spark constructions and Schur-factor methods, without the particular arithmetic classification (1)–(2). Caragea and Lee treat **principal** Fourier minors and do not imply the result for independently chosen four columns. Related established classifications for the adjacent pattern \(\{0,1,2,4\}\), the different pattern \(\{0,1,3,4\}\), and for \(\{0,1,2,5\}\) at prime-power orders do not determine the squarefree family here.

## Limitations
This is a complete exact statement for **one** natural four-row pattern and for moduli \(3p\) with prime \(p\geq5\). It is not an all-pattern composite-order spark criterion. Full spark guarantees noiseless recovery after arbitrary retention of four measurements, but gives no uniform quantitative lower bound on singular values and no stability assertion. Priority relative to uncatalogued special-pattern Fourier-minor literature has not been independently established.

## References
- B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, Theorem 9 and discussion of composite moduli (2011 preprint). https://arxiv.org/abs/1110.3548
- S. R. Garcia, G. Karaali, D. J. Katz, *An Improved Uncertainty Principle for Functions with Symmetry*, arXiv:1807.07648 (first posted 2018-07-19). https://arxiv.org/abs/1807.07648
- R. D. Malikiosis, V. Oussa, *Full Spark Frames in the Orbit of a Representation*, arXiv:1909.06223 (first posted 2019-09-13), especially Section 5. https://arxiv.org/abs/1909.06223
- A. Caragea, D. G. Lee, *On the Principal Minors of Fourier Matrices*, arXiv:2409.09793 (first posted 2024-09-15). https://arxiv.org/abs/2409.09793
