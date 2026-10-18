# Strict Kawasaki freezing and cubic entropy in multicolor Potts rings

## Finding

Fix an integer \(q\ge2\), a ring length \(n\ge3\), and coupling \(J>0\). For labeled colors \(s_i\in\{1,\ldots,q\}\) on the periodic ring, set
\[
H(s)=J\sum_{i=1}^{n}\mathbf1\{s_i\ne s_{i+1}\},\qquad s_{n+1}=s_1.
\]
A configuration is **strictly Kawasaki-blocked** when every exchange of *unequal* neighboring colors strictly increases \(H\). Exchanges with zero energy cost are allowed in the dynamics and therefore preclude blocking. Let \(M(s)\) be the number of domains of length one, and let
\[
B_n^{(q)}(u)=\sum_{s\,\mathrm{blocked}}u^{M(s)}.
\]
The following complete classification and enumeration hold:

1. Every constant-color ring is blocked. Every other blocked ring has domains of length at least two, possibly interrupted by isolated singleton domains. Each singleton is flanked by two domains of length at least two whose colors are *different from each other and from the singleton color*. No two singleton domains are adjacent. These conditions are also sufficient.
2. Define
\[
P_q(z,u)=1-z-(q-1)z^2-(q-1)(q-2)u z^3,\qquad
Q_q(z,u)=1-z+z^2+(q-2)u z^3.
\]
With the formal coefficients for lengths one and two taken to equal \(q\), the complete finite-volume identity is
\[
\boxed{\sum_{n\ge1}B_n^{(q)}(u)z^n
=-z\,\frac{\partial}{\partial z}\log\!\left(P_q(z,u)Q_q(z,u)^{q-1}\right).}
\]
In particular, the physical coefficients for every \(n\ge3\) are exactly those on the right. Equivalently, \(B_n^{(q)}(u)\) is the sum of the \(n\)-th powers of the three roots (with multiplicities) of
\[x^3-x^2-(q-1)x-(q-1)(q-2)u=0\]
plus \(q-1\) times the corresponding sum for
\[x^3-x^2+x+(q-2)u=0.\]
3. For \(u=1\), let \(\alpha_q>1\) be the unique positive root of
\[
\alpha_q^3-\alpha_q^2-(q-1)\alpha_q-(q-1)(q-2)=0.
\]
Then
\[
\boxed{\lim_{n\to\infty}\frac1n\log B_n^{(q)}(1)=\log\alpha_q.}
\]
Under the uniform distribution over strictly blocked length-\(n\) configurations, the singleton-domain density converges in probability to
\[
\boxed{\rho_q=\frac{(q-1)(q-2)}{\alpha_q\left(3\alpha_q^2-2\alpha_q-(q-1)\right)}.}
\]
For \(q=2\), \(\rho_2=0\) and \(\alpha_2=(1+\sqrt5)/2\). For \(q=3\), \(\alpha_3=2.269530842081\ldots\), the entropy is \(0.819573132635\ldots\), and \(\rho_3=0.0988684818069\ldots\). The singletons thus contribute a strictly positive density in the multicolor system, but none can occur in the binary system.

## Assumptions and scope

The dynamics consists of nearest-neighbor *exchanges* of the existing colors, so each color multiplicity is conserved. For every distinct-color neighboring pair, a proposed swap proceeds whenever its energy increment is \(\le0\); thus absorbing states must satisfy *strict* inequalities. Colors are distinguishable, lattice sites are labeled, and cyclic rotations are not identified. No assumption on the initial distribution or on the probability of reaching a blocked state is made. Thermodynamic statements take \(n\to\infty\) at fixed integer \(q\ge2\).

## Proof

For the exchange of a neighboring unequal pair \((b,c)\), write its two exterior colors as \((a,d)\). Direct subtraction of the three affected bonds gives the exact local increment
\[
\frac{\Delta H}{J}=\mathbf1\{a\ne c\}+\mathbf1\{b\ne d\}
-\mathbf1\{a\ne b\}-\mathbf1\{c\ne d\}.
\]
Each of the two differences is \(-1,0\), or \(1\). It follows that \(\Delta H>0\) if and only if (i) \(a\ne c\), (ii) \(d\ne b\), and (iii) at least one of \(a=b\) or \(d=c\) holds. Consequently a boundary between two long (length-at-least-two) color domains is stable. If a domain has length one, applying the condition to its left and right boundaries forces long domains on either side and forces their two colors to differ; conversely that local arrangement makes both exchanges costly. Adjacent singleton domains cannot satisfy the condition, since their common boundary has neither exterior color equal to the corresponding interior color. These observations prove necessity and sufficiency, including uniform rings.

Now mark each long domain and represent a blocked nonconstant ring as a cyclic sequence of \(k\ge2\) long domains with adjacent long-domain colors unequal. A long domain of length \(\ell\ge2\) has weight \(z^\ell\); immediately after it one may optionally insert a single color distinct from both adjacent long-domain colors, with \(q-2\) choices. The weight per long domain and following gap is therefore
\[
t(z,u)=\frac{z^2}{1-z}\left(1+(q-2)uz\right).
\]
The number of proper \(q\)-colorings of a \(k\)-cycle, including the cyclic sequence interpretation for \(k=2\), is
\[
C_k=(q-1)^k+(q-1)(-1)^k.
\]
To pass from a marked cyclic sequence of \(k\) long domains to a labeled ring of size \(n\), choose the position of the first domain in \(n\) ways and divide by the \(k\) possible choices of marked long domain. Therefore the ordinary generating function of all nonconstant blocked rings is
\[
z\frac{d}{dz}\sum_{k\ge1}\frac{C_k}{k}t(z,u)^k
=z\frac{d}{dz}\left[-\log(1-(q-1)t)-(q-1)\log(1+t)\right].
\]
The term \(k=1\) vanishes because \(C_1=0\). Add the \(q\) constant-color rings at every size. Since
\[
1-(q-1)t=\frac{P_q(z,u)}{1-z},\qquad 1+t=\frac{Q_q(z,u)}{1-z},
\]
the \(qz/(1-z)\) contribution of constant words cancels the \(q\log(1-z)\) differentiation, proving the stated rational generating function. Logarithmic differentiation of the factored cubic polynomials yields the root-power identity with algebraic multiplicity.

For \(u=1\), the positive number \(r_q\in(0,1)\) solving \((q-1)t(r_q,1)=1\) is unique, because \(t\) is strictly increasing from zero to infinity. It satisfies \(r_q=1/\alpha_q\). The coefficient set of \(t(z,1)\) contains every power \(z^j\) for \(j\ge2\); the triangle inequality is therefore strict away from the positive real axis on \(|z|=r_q\). Hence \(P_q(z,1)\) has a unique simple zero on this circle. Meanwhile \(|t(z,1)|\le1/(q-1)\le1\) there, and \(1+t\ne0\) on the circle (for \(q=2\), equality in modulus occurs only at the positive real point, where \(t=1\), not \(-1\)). Thus \(Q_q\) has no zero on or inside this circle, and no other singularity competes with the simple pole of the generating function at \(r_q\). Its residue produces \(B_n^{(q)}(1)=\alpha_q^n(1+o(1))\).

The same simple dominant zero depends analytically on \(u\) near \(u=1\). Standard differentiation of the logarithm of the probability generating function \(B_n^{(q)}(u)/B_n^{(q)}(1)\) shows that \(\mathbb E M=n\rho_q+O(1)\) and \(\operatorname{Var}M=O(n)\). Implicit differentiation of the cubic for \(\alpha_q(u)\) gives the displayed \(\rho_q\). Chebyshev's inequality completes convergence in probability.

## Verification

The accompanying `verify_potts_kawasaki.py` implements independent direct Hamiltonian-energy checks, local-increment checks, domain tests, and exact polynomial predictions from Newton sums. It exhaustively compares \(180008\) configurations for \(q=2\) and lengths \(3\) through \(11\), \(q=3\) and lengths \(3\) through \(10\), and \(q=4\) and lengths \(3\) through \(8\). All comparisons passed. Run with Python 3 and SymPy installed: `python verify_potts_kawasaki.py`. These computations check finite cases; the domain and generating-function arguments above establish the infinite-family result.

## Relationship to prior work

De Smedt, Godrèche, and Luck (arXiv:cond-mat/0202465, first public 26 February 2002) compute statistics for three constrained *Ising* chains, including a restricted Kawasaki rule that removes alternating binary patterns. The present problem instead requires all zero-energy exchanges to remain possible, includes every number \(q\ge2\) of Potts colors, and classifies all strictly blocked states; the singleton mechanism for \(q\ge3\) cannot arise in binary Ising. Grynberg (arXiv:1009.4511v1) studies spectra and coarsening exponents for the one-dimensional Kawasaki *Ising* chain, not a multicolor frozen-state polynomial. Krzakala (arXiv:cond-mat/0409348) treats glassy dynamics in two-dimensional Ising and Potts systems, not this exact one-dimensional cyclic enumeration. Thus the current statement is not implied by those inspected results. Other equivalent treatments using directed-word shifts or transfer matrices remain a bibliographic possibility.

## Limitations

The theorem enumerates configurations satisfying *strict* kinetic freezing; it does not describe the distribution of configurations produced by a quench, finite-temperature transitions, mixing rates, or dynamic basins. For \(q\ge3\), fixing species populations can change the entropy and is not treated here. The finite counts are for labeled rings, not rotation classes. Originality has not been independently established against all possible unindexed literature.

## References

1. G. De Smedt, C. Godrèche, J. M. Luck, “Jamming, freezing and metastability in one-dimensional spin systems,” arXiv:cond-mat/0202465 (first public 2002-02-26), https://arxiv.org/abs/cond-mat/0202465.
2. M. D. Grynberg, “Revisiting Kawasaki dynamics in one dimension,” arXiv:1009.4511v1 (first public 2010-09-23), https://arxiv.org/abs/1009.4511.
3. F. Krzakala, “Glassy properties of the Kawasaki dynamics of two-dimensional ferromagnets,” arXiv:cond-mat/0409348 (first public 2004-09-14), https://arxiv.org/abs/cond-mat/0409348.
4. S. J. Cornell, K. Kaski, R. B. Stinchcombe, “Domain scaling and glassy dynamics in a one-dimensional Kawasaki Ising model,” Phys. Rev. B 44, 12263 (1991), doi:10.1103/PhysRevB.44.12263.
