# A quintic frozen-state law for three-row bootstrap-culling cylinders

## Finding

Consider threshold-three bootstrap culling on the nearest-neighbor periodic graph \(C_3\square C_n\), for every integer \(n\ge 3\). A site is occupied or vacant. At each culling step, occupied sites with fewer than three occupied neighbors are deleted; a fixed configuration is one in which no deletion is possible. All four neighbors of a vertex are distinct in the stated range.

For a fixed configuration let \(d\) be its number of columns containing exactly two occupied sites, and \(f\) its number of completely occupied columns. Define the exact fixed-state polynomial
\[
 B_n(a,b)=\sum_{\eta\text{ fixed}}a^{d(\eta)}b^{f(\eta)}.
\]
Let
\[
\begin{aligned}
 \mathsf P(t;a,b)&=1-(1+a+b)t+(a+b-ab)t^2\\
 &\quad +(ab-ab^2-b^2)t^3+2ab^2t^4+2ab^3t^5,\\
 \mathsf Q(t;a,b)&=1-at+abt^2.
\end{aligned}
\]
Then, with the coefficients for \(n=1,2\) interpreted solely as formal transfer-matrix terms,
\[
 \boxed{\displaystyle \sum_{n\ge1}B_n(a,b)t^n=-t\frac{\partial}{\partial t}\log\bigl(\mathsf P(t;a,b)\mathsf Q(t;a,b)^2\bigr).}
\]
In particular \(Z_n(z)=B_n(z^2,z^3)\) counts physical fixed states by total particle number. The totals \(Z_n(1)\) for \(n=3,4,5,6,7,8\) are, respectively, \(17,49,125,323,831,2145\).

Let \(\alpha\) be the Perron root of the recurrent transfer component at unit fugacity. Equivalently, it is the largest positive root of
\[
 \alpha^5-3\alpha^4+\alpha^3-\alpha^2+2\alpha+2=0,
 \qquad \alpha=2.607490996204133\ldots.
\]
The entropy per site of the uniform ensemble of fixed states is exactly
\[
 \boxed{\displaystyle \lim_{n\to\infty}\frac{\log Z_n(1)}{3n}=\frac{\log\alpha}{3}=0.319462818283035\ldots.}
\]
Under the uniform distribution on these fixed configurations, if \(N_n\) denotes the total occupied-site count, then
\[
 \boxed{\displaystyle \frac{N_n}{3n}\xrightarrow{\mathbb P}0.82148891766942\ldots,}
\]
and a central limit theorem holds:
\[
 \boxed{\displaystyle \frac{N_n-n\mu}{\sqrt n}\xrightarrow{d}\mathcal N(0,\sigma^2),\quad
 \mu=2.46446675300826\ldots,\quad\sigma^2=0.4451251123535\ldots.}
\]
The limiting proportions of columns containing respectively zero, two, and three occupied sites are \(0.03832293523749\ldots\), \(0.42056444127927\ldots\), and \(0.54111262348325\ldots\). Thus partially occupied columns form a positive fraction of the typical fixed state; simply counting wholly occupied column blocks would miss the dominant configurations.

## Assumptions and scope

The graph \(C_3\square C_n\) has vertex set \((\mathbb Z/3\mathbb Z)\times(\mathbb Z/n\mathbb Z)\), with nearest neighbors obtained by adding or subtracting one in exactly one coordinate. Throughout \(n\ge3\), so no neighbor is counted twice. Occupation numbers are binary, the threshold is exactly three of four distinct neighbors, boundaries are periodic in both coordinates, and a fixed state means fixed under monotone deletion, not inaccessible under a reversible particle dynamics. \(B_n\) counts labeled-site configurations rather than translation or rotation orbits. The probability laws concern uniform sampling from the fixed-state set, not sampling the endpoint of culling from a Bernoulli initial condition.

## Proof

**Local reduction.** Represent each column by its occupied-row subset of \(\{0,1,2\}\). A column containing exactly one occupied vertex cannot be fixed: that vertex has no occupied vertical neighbor and at most two occupied horizontal neighbors. Hence only five column symbols remain: \(E=\varnothing\), \(F=\{0,1,2\}\), and \(D_j=\{0,1,2\}\setminus\{j\}\), \(j=0,1,2\). For three consecutive columns \(A,B,C\), all occupied vertices in \(B\) are stable exactly under the following local predicate:
\[
  \begin{cases}
   \text{always},&B=E,\\
   A\cup C=F,&B=F,\\
   B\subseteq A\cap C,&B=D_j.
  \end{cases}
\]
Indeed, every occupied site of a full column has two occupied vertical neighbors and needs at least one horizontal occupied neighbor; an occupied site of a double column has one occupied vertical neighbor and needs both horizontal neighbors. These conditions are simultaneously necessary and sufficient.

**Transfer encoding.** Index \(25\) ordered-pair states by \((A,B)\) with \(A,B\in\{E,F,D_0,D_1,D_2\}\). Set
\[
 T_{(A,B),(B,C)}(a,b)=
 \begin{cases}1,& B=E,\\ a,&B=D_j,\\ b,&B=F,\end{cases}
\]
when the displayed local predicate holds, and zero otherwise (all other entries are zero). A closed transfer walk of length \(n\ge3\) is uniquely a cyclic physical column word, and each central column contributes its weight once. Thus \(B_n(a,b)=\operatorname{tr}(T(a,b)^n)\).

Every cyclically admissible adjacent pair is among \((E,E),(E,F),(F,E),(F,F)\) and \((D_j,D_j),(D_j,F),(F,D_j)\) for \(j=0,1,2\). In particular, a double column cannot be adjacent to an empty column or a different double-column type. The other twelve pair states occur on no directed cycle, contributing only zero eigenvalues. The thirteen recurrent states form a strongly connected, aperiodic component when \(a,b>0\): all reach \((F,F)\), all are reachable from \((F,F)\), and \((F,F)\) has a self-loop.

**Exact factorization.** Permuting the three row labels decomposes the recurrent transfer action. On vectors constant on each of the seven pair-type orbits \((EE,EF,FE,FF,DD,DF,FD)\), its matrix is
\[
 M=\begin{pmatrix}
1&1&0&0&0&0&0\\
0&0&0&b&0&0&0\\
1&1&0&0&0&0&0\\
0&0&b&b&0&0&3b\\
0&0&0&0&a&a&0\\
0&0&0&b&0&0&2b\\
0&0&0&0&a&a&0
\end{pmatrix}.
\]
The remaining two standard color representations each have matrix
\[
 R=\begin{pmatrix}a&a&0\\0&0&-b\\a&a&0\end{pmatrix}.
\]
The negative entry is the action on sum-zero color vectors of choosing one of the other two missing-row types; it is a representation coefficient, not a negative transition weight. Direct polynomial determinant expansion gives
\[
\begin{aligned}
\det(\lambda I-M)&=\lambda^2P(\lambda;a,b),\\
\det(\lambda I-R)&=\lambda Q(\lambda;a,b),\\
P(\lambda;a,b)&=\lambda^5-(1+a+b)\lambda^4+(a+b-ab)\lambda^3\\
&\quad +(ab-ab^2-b^2)\lambda^2+2ab^2\lambda+2ab^3,\\
Q(\lambda;a,b)&=\lambda^2-a\lambda+ab.
\end{aligned}
\]
Together with the twelve nonrecurrent zero eigenvalues, this proves the full characteristic-polynomial identity \(\det(\lambda I-T)=\lambda^{16}P(\lambda;a,b)Q(\lambda;a,b)^2\). Using \(\sum_{n\ge1}\operatorname{tr}(T^n)t^n=-t\partial_t\log\det(I-tT)\), and noting \(\mathsf P=t^5P(t^{-1})\), \(\mathsf Q=t^2Q(t^{-1})\), yields the asserted rational logarithmic-derivative identity as a formal power series.

**Thermodynamic limits.** At \(a=b=1\), the recurrent nonnegative matrix is primitive, and the Perron–Frobenius theorem supplies a simple positive leading eigenvalue separated in modulus from the rest. Its eigenvalue belongs to the quintic factor; the quadratic factor has roots of modulus one. It is the displayed \(\alpha\). Consequently \(B_n(1,1)=\alpha^n(1+O(\theta^n))\) for some \(0<\theta<1\), proving the entropy statement.

More generally write \(\lambda(z)\) for the locally analytic Perron eigenvalue of \(T(z^2,z^3)\), normalized by \(\lambda(1)=\alpha\). Let \(\mathscr D=z\,\partial_z\). Then
\[
 \mu=\left.\mathscr D\log\lambda(z)\right|_{z=1},\qquad
 \sigma^2=\left.\mathscr D^2\log\lambda(z)\right|_{z=1}.
\]
Since \(P(\lambda(z);z^2,z^3)=0\), implicit differentiation determines both constants exactly. Analytic perturbation and the spectral gap yield
\[
 \log\mathbb E[e^{tN_n}]=n\log\frac{\lambda(e^t)}{\lambda(1)}+O(\theta^n)
\]
for complex \(t\) near zero, uniformly there. Its second-order expansion proves the law of large numbers and centered normal limit. The variance is strictly positive: in the primitive recurrent graph, the \((E,E)\) and \((F,F)\) self-loops accumulate different occupation rewards, zero and three, which precludes a constant-plus-coboundary reward. Finally, differentiating the leading eigenvalue of \(T(a,b)\) with respect to \(\log a\) and \(\log b\) gives the double- and full-column fractions; the remaining fraction is the empty-column probability.

## Verification

The supplied standard-library `verify.py` independently enumerates all \(2^{3n}\) physical occupancy assignments for each \(n=3,4,5,6\), applies the four-neighbor culling stability test directly, and compares the complete occupancy-graded counts with a separately constructed five-symbol local transfer enumeration. It verifies the exact seven-by-seven and three-by-three characteristic-polynomial identities through integer multivariate polynomial determinants, without relying on numerical eigenvalues. The test passes for \(17,49,125,323\) fixed states, including all occupancy-graded coefficients. A final independent evaluation of the implicit derivatives reproduces the stated Perron root, mean, and variance. Run `python3 verify.py` from any directory with Python 3 and no third-party dependencies. These finite checks supplement, but do not replace, the all-length determinant and Perron arguments above.

## Relationship to prior work

Chalupa, Leath, and Reich introduced bootstrap culling on lattices and trees in 1979. Kogut and Leath examined bootstrap transitions on regular lattices numerically in 1981. Hartarsky and Lichev treat a random-arrival three-core process on growing two-dimensional square tori and its bootstrap dual; their theorem concerns a hitting-time transition, not the labeled fixed-state partition function of a three-row cylinder. Gao, Zhou, and Hu analyze a bootstrap activation process on long-range spatial networks rather than this deterministic culling fixed-state enumeration. The transfer-matrix technique itself is classical and is not claimed as new. Targeted comparisons identified no source establishing this particular quintic fugacity polynomial, its exact coefficients for all cylinder lengths, and the associated uniform fixed-state occupation law. See the originality review for access limits.

## Limitations

No theorem here determines the distribution of endpoints reached from independently occupied initial sites, the culling time, or a large-width limit. The occupation density is that of the uniform ensemble of fixed configurations. The \(n=1,2\) formal series coefficients are not physical square-neighbor counts because those graphs have repeated horizontal neighbors. The primary 1979 and 1981 publisher papers were not accessible in full through available routes; unrecognized earlier enumeration remains a bibliographic risk. No independent audit has been performed.

## References

1. J. Chalupa, P. L. Leath, and G. R. Reich, *Bootstrap percolation on a Bethe lattice*, Journal of Physics C 12 (1979), L31–L35. DOI: `10.1088/0022-3719/12/1/008`.
2. P. M. Kogut and P. L. Leath, *Bootstrap percolation transitions on real lattices*, Journal of Physics C 14 (1981), 3187. DOI: `10.1088/0022-3719/14/22/013`.
3. I. Hartarsky and L. Lichev, *Explosive appearance of cores and bootstrap percolation on lattices*, Combinatorica 46 (2026), article 17. DOI: `10.1007/s00493-026-00213-2` (open-access full text inspected).
4. J. Gao, T. Zhou, and Y. Hu, *Bootstrap percolation on spatial networks*, Scientific Reports 5 (2015), 14662. DOI: `10.1038/srep14662` (open-access full text inspected).
