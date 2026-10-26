# Finite étale generation profiles and an arithmetic compound-Poisson defect law

## Finding

Fix a prime power \(q\ge2\), an integer \(m\ge1\), and \(E=\mathbb F_{q^m}\). For integers \(r,\ell\ge1\), choose \(\ell\) independent uniform elements of the unital \(\mathbb F_q\)-algebra \(A=E^r\). Let \(B\) be the unital subalgebra that they generate.

For each positive divisor \(d\mid m\), define the nonnegative integer
\[
h_d=\frac1d\sum_{e\mid d}\mu(e)q^{d\ell/e},
\]
where \(\mu\) is the Möbius function. There exist unique random nonnegative integers \(S_d\) such that
\[
 B\cong_{\mathbb F_q}\prod_{d\mid m}(\mathbb F_{q^d})^{S_d}.
\]
Their *entire joint probability distribution*, including zero-multiplicity factors, is specified by the formal exponential generating series
\[
\boxed{\sum_{r\ge0}\frac{q^{m\ell r}}{r!}\,\mathbb E\!\left[\prod_{d\mid m}z_d^{S_d}\right]t^r
 =\prod_{d\mid m}\left(1+z_d(e^{dt}-1)\right)^{h_d}.}
\]
The \(r=0\) summand is a formal combinatorial convention; the stated random algebra is defined for \(r\ge1\). In particular, \(\dim_{\mathbb F_q}B=\sum_{d\mid m}dS_d\), so this also gives its complete dimension distribution.

There is a sharp *two-mechanism limiting law*. Keep \(q,m\) fixed, let \(\ell\to\infty\), and take positive integers \(r_\ell\) with \(r_\ell/q^{m\ell/2}\to c\in[0,\infty)\). Put
\[
 L_\ell=mr_\ell-\dim_{\mathbb F_q}B_\ell.
\]
Then
\[
\boxed{L_\ell\ \xrightarrow{\mathrm d}\ mX+\mathbf1_{2\mid m}\frac m2Y,}
\]
where \(X\) and \(Y\) are **independent**, with \(X\sim\operatorname{Poisson}(mc^2/2)\) and \(Y\sim\operatorname{Poisson}(c)\). When \(m\) is odd, the second term is absent. The first term records collisions between Frobenius-conjugate full-degree coordinate tuples. The second records individual coordinate tuples falling into the index-two proper subfield when \(m\) is even.

## Assumptions and scope

The base field \(\mathbb F_q\) may be any finite prime-power field. All algebra generation is *unital* and over \(\mathbb F_q\). The variables \(r,\ell,m\) are positive integers; random generators are independent and uniformly distributed in \(A\), with repeated values allowed. The exact series is an identity in the formal power series ring \(\mathbb Q[z_d:d\mid m][[t]]\) for fixed \(q,m,\ell\). The limit fixes \(q,m\) while \(r\) and \(\ell\) vary as stated; the point \(c=0\) is included. No statement about a varying field size or varying extension degree is made.

An \(\ell\)-tuple in \(E^\ell\) has *degree* \(d\mid m\) if its smallest common field of definition over \(\mathbb F_q\) is \(\mathbb F_{q^d}\); equivalently, its orbit under coordinatewise Frobenius \(x\mapsto x^q\) has length \(d\).

## Proof

**1. Reconstruction of generated subalgebras.** Write the chosen generators as \(a_1,\ldots,a_\ell\in E^r\) and form the column tuples \(v_i=(a_{1i},\ldots,a_{\ell i})\in E^\ell\), \(1\le i\le r\). The evaluation homomorphism
\[
 \phi:\mathbb F_q[T_1,\ldots,T_\ell]\longrightarrow E^r,
 \qquad f\longmapsto(f(v_1),\ldots,f(v_r))
\]
has image \(B\). The kernel of the \(i\)-th coordinate evaluation is a maximal ideal with residue field \(\mathbb F_q(v_i)=\mathbb F_{q^{d_i}}\). Two kernels coincide exactly when \(v_i\) and \(v_j\) are coordinatewise Frobenius-conjugate: one implication is clear; conversely, identical kernels identify their residue fields and the images of all coordinate variables, so the two embeddings of the common finite residue field into \(E\) differ by a Frobenius automorphism. Distinct kernels are comaximal, so the Chinese remainder theorem yields
\[
B\cong\mathbb F_q[T_1,\ldots,T_\ell]/\bigcap_i\ker(\operatorname{ev}_{v_i})
\cong\prod_{\mathcal O\ \mathrm{occupied}}\mathbb F_{q^{|\mathcal O|}}.
\]
This proves the classification and dimension assertion.

**2. Exact occupancy polynomial.** There are exactly \(q^{d\ell}\) tuples with all coordinates in \(\mathbb F_{q^d}\), so Möbius inversion gives \(d h_d=\sum_{e\mid d}\mu(e)q^{d\ell/e}\). Each Frobenius orbit of length \(d\) contains \(d\) possible column tuples. Assigning any positive number \(k\) of labelled coordinates to this one orbit gives \(d^k\) assignments, with exponential generating series \(e^{dt}-1\). Choosing no coordinate gives weight \(1\); choosing at least one gives \(z_d(e^{dt}-1)\). Multiplying independently over all \(h_d\) orbits, and observing that all \((q^{m\ell})^r\) arrays of column tuples are equiprobable, proves the boxed generating series. Its total-mass specialization is \(e^{q^{m\ell}t}\), since \(\sum_{d\mid m}d h_d=q^{m\ell}\), as required.

**3. Rare subfield coordinates.** Set \(N=q^{m\ell}\). If \(m\) is even, the number of columns belonging to \(\mathbb F_{q^{m/2}}^\ell\) is binomial with \(r_\ell\) trials and probability \(N^{-1/2}\), hence converges to \(Y\sim\operatorname{Poisson}(c)\). Every other proper subfield has size at most \(q^{m/3}\), apart from the index-two field itself. A union bound over the finitely many proper divisors shows that the expected number of columns of degree below \(m\) but not exactly \(m/2\) is \(O(r_\ell N^{-2/3})=o(1)\). A column in the index-two field has degree exactly \(m/2\) except on an event of vanishing total probability. If \(m\) is odd, every proper divisor is at most \(m/3\), so the expected number of columns of degree below \(m\) is \(o(1)\). The statement also covers \(m=1\), where there is no proper subfield.

**4. Full-degree orbit collisions.** The number of length-\(m\) Frobenius orbits is \(h_m=N/m+O(N^{1/2})\), except that at \(m=1\) it is exactly \(N\). Conditional on the number of non-full-degree columns, the full-degree columns have independent uniform orbit labels from these \(h_m\) possibilities. Their number is \(r_\ell-O_{\mathbb P}(1)\). Let \(C_\ell\) count unordered pairs with equal full-degree orbit labels. Its factorial moments obey
\[
 \mathbb E[(C_\ell)_k]\longrightarrow (mc^2/2)^k
 \qquad\text{for each fixed }k\ge1,
\]
since disjoint pairs dominate, while configurations with a connected collision cluster of at least three labels contribute \(O(r_\ell^3/h_m^2)=o(1)\) (higher connected patterns are smaller). Hence \(C_\ell\Rightarrow\operatorname{Poisson}(mc^2/2)\). The factorial-moment estimates are uniform when the conditioned count of subfield columns is bounded; tightness of that count gives asymptotic independence between \(C_\ell\) and \(Y\). Moreover, with probability tending to one no full-degree orbit is visited three or more times, so \(mr_\ell-mS_m=mC_\ell\) after excluding subfield columns.

**5. Dimension defect.** The number of subfield columns is tight. Their degree-\(m/2\) orbit labels, when relevant, are mutually distinct with probability tending to one: the number of such orbit labels \(h_{m/2}\) tends to infinity. On the event whose probability tends to one described above, each such column contributes a deficit \(m-m/2=m/2\), while each full-degree pair collision contributes \(m\). Combining the two independent Poisson limits proves the limit law. The equality \(h_m=N/m+O(N^{1/2})\) suffices uniformly for fixed \(q,m\). At \(c=0\), the same rare-event estimates imply convergence to zero.

## Verification

A standalone standard-library Python checker (`checker.py`) directly constructs finite extension-field operations, enumerates all generator arrays in eight small configurations, and independently computes the generated algebra by repeated linear-span closure. It then counts idempotents to check the number of field factors, computes Frobenius-orbit profiles, and compares *every* profile frequency with the exponential-series coefficient formula. The eight cases encompass \(q=2,3\), \(m=1,2,3\), one and two generators, and up to three algebra factors. The total is 16,403 enumerated arrays; all profile and algebra tests passed. The limiting Poisson claim is proved analytically, not by finite enumeration.

## Relationship to prior work

Kravchenko, Mazur and Petrenko (arXiv:1001.2873, Theorems 6.1 and 6.3, and Proposition 6.2) established the orbit-separation criterion for generating an *entire* direct power of a simple finite algebra and an exact formula for the number of full generating tuples. That full-generation count is prior work and is not the novelty asserted here. Sercombe and Shalev (arXiv:2009.01115, first posted 2020-09-02) studied random generation and generator thresholds for finite associative algebras. Their reviewed results concern full generation, minimal generator counts, and related probabilities, not the full random *isomorphism-type profile* of all generated subalgebras or its parity-dependent dimension-defect distribution.

The present theorem refines the one-bit full-generation event to a multivariate distribution recording every proper-degree field factor, and connects this refinement to a two-source compound-Poisson limit. Its ingredients include classical finite-field Frobenius descent, the Chinese remainder theorem, and occupancy asymptotics. The existence of an older equivalent all-type enumeration remains an unresolved priority risk; the comparison is not a claim of historical uniqueness.

## Limitations

The result is restricted to commutative finite étale algebras that are equal-field direct powers; extension to different field-factor degrees or matrix factors is not proved. The asymptotic holds with fixed \(q,m\) only. The code verifies finitely many small configurations and cannot certify the asymptotic law. The originality assessment is limited by the available primary literature; classical orbit and full-generation formulas are explicitly not claimed as new. Independent mathematical validation has not been performed.

## References

1. D. Sercombe and A. Shalev, *Random generation of associative algebras*, arXiv:2009.01115 (initial public version 2020-09-02); *J. London Math. Soc.* 109 (2024), e12827; DOI 10.1112/jlms.12827. https://arxiv.org/abs/2009.01115
2. R. V. Kravchenko, M. Mazur, and B. V. Petrenko, *On the smallest number of generators and the probability of generating an algebra*, arXiv:1001.2873 (2010); *Algebra Number Theory* 6 (2012), 243–291. Theorems 6.1 and 6.3, Proposition 6.2. https://arxiv.org/abs/1001.2873
