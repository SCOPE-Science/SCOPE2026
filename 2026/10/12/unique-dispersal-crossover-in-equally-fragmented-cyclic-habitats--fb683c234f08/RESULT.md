# Unique dispersal crossover in equally fragmented cyclic habitats

## Finding

Consider a homogeneous nearest-neighbor dispersal model on a circular chain of habitats. Let the two periodic binary habitat profiles, indexed from zero, be

\[
A=(0,0,0,1,0,0,1,1,1),\qquad
B=(0,0,0,0,1,1,0,1,1).
\]

For any integer \(r\geq 1\), repeat either nine-cell pattern \(r\) times around a cycle of length \(9r\). Let \(L_{9r}\) denote the ordinary combinatorial Laplacian of that cycle and put

\[
M_s(b,g,d)=bI+g\operatorname{diag}(s)-dL_{9r},
\qquad b\in\mathbb R,\quad g>0,\quad d>0.
\]

Write \(\lambda_s(b,g,d)\) for its largest real eigenvalue, the exponential growth rate of the associated linear population system. Both landscapes have the same suitable-habitat fraction \(4/9\), exactly \(2r\) suitable-habitat components and exactly \(4r\) interfaces between favorable and unfavorable cells. In each period the favorable-component lengths are \((1,3)\) for \(A\) and \((2,2)\) for \(B\).

**Theorem.** There is one and only one constant \(\delta_*\in(4,5)\), numerically \(\delta_*\approx 4.00252242784\), such that for every integer \(r\geq1\), every \(g,d>0\), and every \(b\in\mathbb R\),

\[
\begin{aligned}
\lambda_A(b,g,d)&>\lambda_B(b,g,d)&&\text{if }0<d/g<\delta_*,\\
\lambda_A(b,g,d)&=\lambda_B(b,g,d)&&\text{if }d/g=\delta_*,\\
\lambda_A(b,g,d)&<\lambda_B(b,g,d)&&\text{if }d/g>\delta_*.
\end{aligned}
\]

The exact constant is specified without numerical fitting. Let \(\Lambda_B(t)\) be the top eigenvalue of \(\operatorname{diag}(B)-tL_9\). Then \(\delta_*\) is the unique positive solution of

\[
\Lambda_B(t)=\frac{t^2-4t+1}{2}.
\]

The comparison concerns linearized population growth, not nonlinear persistence or observed population abundance.

## Assumptions and scope

All chains use undirected nearest-neighbor edges with the same positive dispersal intensity \(d\). Each favorable cell has additional local per-capita growth \(g\) above baseline \(b\), and unfavorable cells have no such addition. Sites may receive population from neighboring sites irrespective of habitat quality. The population dynamics are \(\dot u=M_s(b,g,d)u\) with nonnegative, nonzero initial density. The graph is a simple cycle, and \(r\geq1\); because \(9r\geq9\), the two neighbors of each cell are distinct.

For irreducible Metzler growth matrices, the dominant eigenvalue controls the eventual exponential rate for strictly positive initial states (and for all nonzero nonnegative initial states). No density dependence, demographic noise, environmental switching, or edge heterogeneity is included. The theorem compares exactly the stated two landscape configurations and their periodic repetitions, not every placement of four favorable cells among nine.

## Proof

**1. Eliminate repetition and growth-unit choices.** For any positive \(d\), adding a sufficiently large scalar multiple of the identity turns \(M_s\) into an irreducible nonnegative matrix. Perron--Frobenius implies its top eigenvalue is simple with an entrywise positive eigenvector. For a profile repeated with period nine, rotating the ring by nine sites commutes with \(M_s\). Uniqueness of the normalized positive eigenvector forces that eigenvector to be nine-periodic. Its restriction to one period satisfies the nine-cell eigenproblem, and its eigenvalue is the nine-cell top eigenvalue. Hence for both patterns and all \(r\),

\[
\lambda_s(b,g,d)=b+g\Lambda_s(d/g),\qquad
\Lambda_s(t)=\lambda_{\max}(\operatorname{diag}(s)-tL_9).
\]

It is therefore enough to compare \(\Lambda_A(t)\) and \(\Lambda_B(t)\) for \(t>0\).

**2. Monotonicity and strict spectral bounds.** The Rayleigh variational principle, tested on the all-ones vector, gives \(\Lambda_s(t)\geq4/9\). Equality would force the constant vector to maximize the Rayleigh quotient and hence be an eigenvector, which is impossible because \(s\) is nonconstant; therefore \(\Lambda_s(t)>4/9\). Conversely, the potential term is at most one and the Laplacian penalty is nonnegative; equality \(\Lambda_s(t)=1\) would require an eigenvector both supported entirely on favorable sites and constant along all edges, impossible on a connected cycle. Thus

\[
4/9<\Lambda_s(t)<1\qquad(t>0).
\]

The simple-eigenvalue derivative formula gives

\[
\Lambda_s'(t)=-v(t)^{\mathsf T}L_9v(t)
=-\sum_{i=0}^{8}(v_i(t)-v_{i+1\bmod9}(t))^2<0
\]

for a unit positive Perron eigenvector \(v(t)\); equality would require a constant Perron vector, again impossible. In particular \(\Lambda_B\) is continuous and strictly decreasing.

**3. Exact characteristic-polynomial cancellation.** Define the characteristic polynomial

\[
P_s(z,t)=\det(zI_9-\operatorname{diag}(s)+tL_9).
\]

Write \(K(v_i,\ldots,v_j)\) for the determinant of the tridiagonal path matrix with diagonal entries \(z+2t-v_k\) and neighboring entries \(-t\); adopt \(K(\varnothing)=1\). Successive terminal expansion yields the continuant recurrence

\[
K(v_i,\ldots,v_j)=(z+2t-v_j)K(v_i,\ldots,v_{j-1})-t^2K(v_i,\ldots,v_{j-2}).
\]

Expanding the two corner entries in the nine-cell cyclic determinant gives

\[
P_s(z,t)=K(v_0,\ldots,v_8)-t^2K(v_1,\ldots,v_7)-2t^9.
\]

Substituting the two explicit profiles in this recurrence and collecting exact integer coefficients gives the identity

\[
\boxed{P_A(z,t)-P_B(z,t)=t^4(2t+z)(t^2-4t-2z+1).}
\tag{1}
\]

A standalone exact-integer polynomial checker recomputes both continuants and verifies every coefficient in (1); no floating-point approximation is involved in this identity.

**4. The only possible crossing.** If \(\Lambda_A(t)=\Lambda_B(t)=z\), both characteristic polynomials vanish. Since \(z>4/9\) and \(t>0\), identity (1) implies

\[
z=q(t):=\frac{t^2-4t+1}{2}.
\tag{2}
\]

For \(0<t\leq4\), \(q(t)\leq1/2\). To show that \(\Lambda_B(t)>1/2\) on this entire interval, use the integer test vector

\[
w=(9,8,8,9,11,12,11,12,11).
\]

At \(t=4\), its exact Rayleigh quotient is

\[
\frac{w^{\mathsf T}(\operatorname{diag}(B)-4L_9)w}{w^{\mathsf T}w}
=\frac{474}{941}>\frac12.
\]

As \(\Lambda_B\) is decreasing, \(\Lambda_B(t)\geq\Lambda_B(4)>1/2\) for \(0<t\le4\). For \(t\ge4\), \(q'(t)=t-2>0\) while \(\Lambda_B'(t)<0\), so (2) has at most one solution. Such a solution exists strictly between four and five: \(q(4)=1/2<\Lambda_B(4)\), whereas \(q(5)=3>1>\Lambda_B(5)\). Call the unique solution \(\delta_*\). Thus the two *top* eigenvalue curves can meet at most once.

**5. Determine the direction on both sides.** Let \(\eta=2-2\cos(2\pi/9)\) be the first nonzero eigenvalue of \(L_9\). One has \(\eta>2/5\). Indeed \(c=\cos(2\pi/9)\) lies between \(1/2\) and one and satisfies \(4c^3-3c+1/2=0\); this cubic increases for \(c>1/2\) and is positive at \(c=4/5\), hence \(c<4/5\). Weyl's eigenvalue bound therefore yields

\[
\lambda_2(\operatorname{diag}(A)-tL_9)
\leq1-t\eta<1-\frac{2t}{5}.
\]

At \(t=1\), the positive integer vector \(u=(2,1,1,2,4,5,3,5,4)\) gives

\[
\Lambda_B(1)\geq\frac{u^{\mathsf T}(\operatorname{diag}(B)-L_9)u}{u^{\mathsf T}u}
=\frac{62}{101}>\frac35>\lambda_2(\operatorname{diag}(A)-L_9).
\]

At \(t=5\), the second eigenvalue for \(A\) is less than \(-1\), while \(\Lambda_B(5)>4/9\). At these two test intensities the value \(z=\Lambda_B(t)\) is therefore greater than every eigenvalue of the \(A\)-matrix except possibly its largest. Consequently the sign of \(P_A(\Lambda_B(t),t)\) is the sign of \(\Lambda_B(t)-\Lambda_A(t)\). Equation (1), evaluated at \(z=\Lambda_B(t)\), gives the sign of \(q(t)-\Lambda_B(t)\). At \(t=1\) this is negative, so \(\Lambda_A(1)>\Lambda_B(1)\). At \(t=5\) it is positive, so \(\Lambda_A(5)<\Lambda_B(5)\).

Both largest-eigenvalue curves are continuous and have exactly one possible common point. Since their ordering differs at \(t=1\) and \(t=5\), they meet precisely at \(\delta_*\), with the stated strict order on each side. Step 1 transports the conclusion to all repetitions and all allowed \(b,g,d\). \(\square\)

## Verification

Run the complete standalone script `python3 verify_model.py` using Python 3 and its standard library. It independently constructs exact bivariate characteristic polynomials through the continuant recurrence, checks identity (1) coefficient by coefficient, verifies the two rational Rayleigh witnesses, and confirms the favorable-site/interface counts. As auxiliary nonproof checks it computes positive Perron eigenvectors by shifted power iteration, samples the ordering at several dispersal intensities, and checks that two- and three-period repetitions have the same top eigenvalues. It locates the crossing numerically inside \((4.0025,4.0026)\). Numerical tests are not used to prove the unique-for-all-real-parameters statement; steps 1--5 are the proof.

## Relationship to prior work

The ecological distinction between habitat *amount* and *arrangement* motivates the model: Flather and Bevers (2002) report nonlinear, finite-capacity simulated population responses across random landscapes, including effects of aggregation and edge length. Their full article presents a different model and does not give an all-dispersal spectral ranking of the two stated nine-site patterns. Berestycki, Hamel and Roques (2005) provide the continuous periodically fragmented reaction--diffusion persistence framework. Nadin (2010; accessible arXiv version 2016) proves that one-dimensional Schwarz rearrangement improves the periodic principal eigenvalue in a continuous-domain setting. Liang (2026) reports a cyclic bell-shaped optimization theorem for nearest-neighbor periodic lattice operators; its available abstract describes a global optimizer, not the exact comparison of two noncontiguous equal-interface layouts.

The present result is neither a general rearrangement theorem nor a claim that the favorable site count or number of clusters alone identifies population growth. In fact it exhibits why those summary statistics do not order even two natural two-patch layouts uniformly over dispersal intensity. Recasting a fixed operator's largest eigenvalue as the growth rate is standard; the contribution assessed here is the exact cancellation (1), resulting unique crossover, and repetition-uniform classification for these landscapes.

## Limitations

This is an exact theorem for a deliberately specified pair of deterministic linear environments. Neither numerical evidence nor the present proof establishes uniqueness of a crossing for other profiles. A dominant linear growth rate is not equivalent to nonlinear long-term persistence under density dependence or stochastic environmental events. The crossover value is defined exactly by an eigenvalue equation; its displayed decimal is approximate. Previously published full coverage cannot be absolutely excluded; the specifically relevant earlier papers and remaining access limitations are documented in the accompanying review.

The earliest source record used for age classification is the bibliographic date `2002-01-01` recorded for Flather--Bevers by OpenAlex (`W2142084183`). The journal and PubMed specify January 2002 only, not an individually verified first-of-month release; that date is an index convention, not a claimed day of first dissemination.

## References

1. C. H. Flather and M. Bevers, *Patchy Reaction--Diffusion and Population Abundance: The Relative Importance of Habitat Amount and Arrangement*, American Naturalist 159 (2002), 40--56. DOI `10.1086/324120`. Lawful full text: `https://research.fs.usda.gov/download/treesearch/23752.pdf`. Bibliographic date: `https://openalex.org/W2142084183`.
2. H. Berestycki, F. Hamel and L. Roques, *Analysis of the periodically fragmented environment model: I--Species persistence*, Journal of Mathematical Biology 51 (2005), 75--113. DOI `10.1007/s00285-004-0313-3`.
3. G. Nadin, *The Effect of the Schwarz Rearrangement on the Periodic Principal Eigenvalue of a Nonsymmetric Operator*, SIAM Journal on Mathematical Analysis 41 (2010). DOI `10.1137/080743597`. Accessible full text: `https://arxiv.org/html/1609.01442v1`.
4. X. Liang, *Variational Principles and Rearrangement Inequalities for Asymmetric Operators on Periodic Lattices*, arXiv `2608.11986` (2026). Abstract `https://arxiv.org/abs/2608.11986`; full text could not be inspected.
