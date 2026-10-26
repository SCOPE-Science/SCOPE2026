# A first repeated-node resonance in the lattice Fourier zeros of the standard 4-simplex

## Finding

Let
\[
\Delta_4=\{x\in\mathbb R^4:x_j\ge0,\ x_1+x_2+x_3+x_4\le1\},\qquad
F(\xi)=\int_{\Delta_4}e^{-2\pi i\langle\xi,x\rangle}\,dx.
\]
For \(k=(k_1,k_2,k_3,k_4)\in\mathbb Z^4\), form the multiset
\[
M(k)=\{0,k_1,k_2,k_3,k_4\}.
\]
Then \(F(k)=0\) if and only if either (i) the five entries of \(M(k)\) are pairwise distinct, or (ii) there are integers \(a\) and \(d\ne0\) such that
\[
M(k)=\{a,a,a+d,a+2d,a+2d\}
\]
as multisets. In the second case, the middle of three equally spaced integer values occurs once and each endpoint occurs twice. This is the complete zero classification on the integer frequency lattice for the standard 4-simplex. It also identifies dimension four as the first simplex dimension with a repeated-node lattice zero.

## Assumptions and scope

The transform uses negative-exponential convention \(e^{-2\pi i\langle\xi,x\rangle}\) and unnormalized four-dimensional Lebesgue measure. Frequencies are restricted to \(\mathbb Z^4\); the result is not a classification of the full real or complex zero set. The simplex is the standard coordinate simplex, not an arbitrary affine simplex. Multiplicities in \(M(k)\) are retained. The zero at the origin is excluded automatically because all five nodes then coincide and \(F(0)=\operatorname{vol}(\Delta_4)=1/24\).

## Proof

**1. Exponential-simplex divided difference.** Put \(c=-2\pi i\) and \(z_j=ck_j\) for \(j=1,\ldots,4\), with \(z_0=0\). The exponential-simplex formula gives
\[
F(k)=[z_0,z_1,z_2,z_3,z_4]e^z,
\]
where the right side is the divided difference, interpreted confluent when nodes coincide. If the five integer nodes are distinct, then \(e^{z_j}=1\) for all \(j\), so the divided difference equals the fourth divided difference of the constant function \(1\), which is zero.

**2. Exact residue polynomial for repeated nodes.** Let the distinct integer values in \(M(k)\) be \(a\), with multiplicities \(m_a\), so \(\sum_a m_a=5\). The confluent divided difference is the sum of residues of
\[
\frac{e^z}{\prod_a(z-ca)^{m_a}}.
\]
Since \(e^{ca}=1\), setting \(z=ca+y\) and \(s=1/c=i/(2\pi)\) yields
\[
F(k)=P(s),\qquad
P(s)=\sum_a s^{5-m_a}[y^{m_a-1}]\left(e^y\prod_{b\ne a}(a-b+sy)^{-m_b}\right).
\]
Here \([y^r]\) means coefficient extraction. Every coefficient in \(P\) is rational because the nodes are integers and the expansions are finite to the required order. The number \(s=i/(2\pi)\) is transcendental; therefore a rational-coefficient polynomial \(P\) vanishes at \(s\) exactly when it is the zero polynomial.

**3. Multiplicity classification.** The repeated partitions of five are \(5\), \(4+1\), \(3+2\), \(3+1+1\), \(2+1+1+1\), and \(2+2+1\). In each pattern except \(2+2+1\), one node has unique maximal multiplicity, say \(m_a\). The lowest power \(s^{5-m_a}\) in \(P\) then has coefficient
\[
\frac{1}{(m_a-1)!}\prod_{b\ne a}(a-b)^{-m_b},
\]
which is nonzero. Thus these patterns cannot produce a zero.

It remains to consider two repeated nodes \(a,b\) and one singleton \(u\). The coefficient of the lowest power \(s^3\) is
\[
\frac{1}{(a-b)^2}\left(\frac1{a-u}+\frac1{b-u}\right)
=\frac{a+b-2u}{(a-b)^2(a-u)(b-u)}.
\]
If \(u\ne(a+b)/2\), this coefficient is nonzero, so \(P\not\equiv0\) and \(F(k)\ne0\). If \(u=(a+b)/2\), write the three values as \(u-d,u,u+d\), where \(d\in\mathbb Z\setminus\{0\}\). After scaling and translating the complex nodes, the residue calculation reduces to the multiset \(\{-h,-h,0,h,h\}\), where \(h=cd\) and \(e^{h}=e^{-h}=1\). The residues at \(-h\), \(0\), and \(h\) are respectively
\[
-\frac1{4h^3}-\frac1{2h^4},\qquad \frac1{h^4},\qquad
\frac1{4h^3}-\frac1{2h^4}.
\]
Their sum is zero. Hence the transform vanishes precisely for the stated endpoint-midpoint-endpoint multiplicity pattern.

For dimensions at most three, there are at most four nodes. Every repeated pattern has a unique largest multiplicity except the two-pair pattern. Its two residues, after centering the nodes, sum to a nonzero constant multiple of \(h^{-2}\). Thus no repeated-node lattice zero occurs below dimension four.

## Verification

The included standard-library checker expands the confluent-residue formula exactly over the rationals. It checked all 210 five-node multisets drawn from \(\{-3,-2,-1,0,1,2,3\}\) that contain zero. Exactly 20 residue polynomials were identically zero: 15 all-distinct patterns and five repeated-node patterns, all of the claimed arithmetic-progression form. It also verifies the exceptional identity and a nonzero control polynomial. This finite check is diagnostic; the multiplicity argument above proves the classification for all integer frequencies.

## Relationship to prior work

Baldoni, Berline, De Loera, Köppe and Vergne present Brion's exponential-simplex vertex formula in Corollary 12 of *How to Integrate a Polynomial over a Simplex*. Borda gives a separate representation of the Fourier transform of an arbitrary simplex and explicitly discusses coincident vertex projections and higher-order residues. These are the general transform tools used here; neither inspected statement gives the integer-lattice zero classification or its exceptional repeated-node pattern. Kolountzakis and Spyridakis study which complex varieties can lie in the zero set of a polytope's Fourier–Laplace transform, but their results concern entire spheres and parametrized curves, not this discrete lattice slice.

## Limitations

The classification is only for the standard 4-simplex and integer frequencies. No claim is made for arbitrary simplex shapes, noninteger frequencies, or dimensions five and higher, where additional multiplicity partitions may arise. The conclusion uses the transcendence of \(\pi\) to exclude accidental zeros of nonzero rational-coefficient residue polynomials. The exact transform formula is classical; the contribution is the complete zero-set classification in this specified lattice slice. Publication priority is not independently certified.

## References

1. V. Baldoni, N. Berline, J. A. De Loera, M. Köppe and M. Vergne, *How to Integrate a Polynomial over a Simplex*, arXiv:0809.2083v1, first submitted 11 September 2008, Corollary 12, formula (10), and Remark 15. https://arxiv.org/abs/0809.2083
2. Bence Borda, *Lattice points in algebraic cross-polytopes and simplices*, arXiv:1608.02417v1, first submitted 8 August 2016, Section 2.3, Theorem 3. https://arxiv.org/abs/1608.02417
3. Mihail N. Kolountzakis and Emmanuil Spyridakis, *Curves in the Fourier zeros of polytopal regions and the Pompeiu problem*, arXiv:2404.03405v1, first submitted 4 April 2024, Sections 1–3. https://arxiv.org/abs/2404.03405
4. Tianjuan Yang, Xiuguo Chen, Jiahao Zhang, Jianyuan Ma and Shiyuan Liu, *Form factor of any polyhedron and its singularities derived from a projection method*, Journal of Applied Crystallography 56 (2023), 167–177, DOI 10.1107/S160057672201130X. The accessible abstract concerns singularities of the form-factor formula, not a stated integer-lattice zero classification.
