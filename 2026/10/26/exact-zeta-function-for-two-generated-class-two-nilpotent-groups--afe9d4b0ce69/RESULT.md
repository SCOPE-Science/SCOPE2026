# Exact zeta function for two-generated class-two nilpotent groups

## Finding

Let \(g(n,2,2)\) be the number of isomorphism classes of finite nilpotent groups \(G\) with \(|G|=n\), nilpotency class at most two, and at most two generators. The Dirichlet generating function is

\[
\zeta_{2,2}(s):=\sum_{n\ge 1}g(n,2,2)n^{-s}
=\zeta(s)\zeta(2s)\zeta(3s)^2\zeta(4s),\qquad \operatorname{Re}(s)>1,
\]

where \(\zeta\) denotes the Riemann zeta function. Equivalently, for every prime \(p\), the local factor is

\[
\sum_{k\ge0}g(p^k,2,2)t^k
=\frac{1}{(1-t)(1-t^2)(1-t^3)^2(1-t^4)}.
\]

In particular, the local coefficients do not depend on the prime: \(g(p^k,2,2)\) is the number of nonnegative integer solutions of \(a+2b+3c+3d+4e=k\). The product also has a simple pole at \(s=1\), giving the summatory asymptotic

\[
\sum_{m\le x}g(m,2,2)\sim \frac{\pi^6\zeta(3)^2}{540}\,x.
\]

## Assumptions and scope

Groups are counted up to isomorphism, not as labeled multiplication tables. “Class at most two” includes abelian groups, and “at most two generators” includes cyclic groups and the trivial group. The Dirichlet series is initially defined by its sum in the half-plane \(\operatorname{Re}(s)>1\). The local formula is valid for every prime, including \(p=2\).

## Proof

Every finite nilpotent group is the direct product of its Sylow subgroups. The count \(g(n,2,2)\) is therefore multiplicative in \(n\), and the global Dirichlet series has an Euler product with local factor

\[
\zeta_{2,2,p}(s)=\sum_{k\ge0}g(p^k,2,2)p^{-ks}.
\]

For a fixed prime \(p\), each group in this local family is a quotient of the pro-\(p\) completion of the free nilpotent group of class two on two generators. Isomorphism classes of quotients correspond to automorphism orbits of finite-index normal subgroups. Using the associated Heisenberg Lie ring \(L\), with basis \(x,y,z\) and bracket \([x,y]=z\), Voll translates the orbit problem into classifying finite-index ideals of \(L\otimes\mathbb Z_p\) under its automorphism group.

Represent a full lattice by its upper-triangular Hermite-normal-form matrix. The ideal condition and the automorphism action yield a unique representative for each double coset with parameters \(e_1,\ldots,e_5\in\mathbb Z_{\ge0}\) satisfying

\[
0\le e_4,e_5\le e_3,\qquad e_5\le e_4\le e_5+e_1.
\]

The corresponding index is \(p^{e_1+2e_2+3e_3}\). The normal-form existence follows by putting the upper-left \(2\times2\) block into Smith normal form and normalizing the last-column entries; uniqueness follows from the diagonal valuations, the valuation of the last column, and the permitted elementary row/column operations. This is the substantive orbit-classification step; it is not supplied by finite enumeration.

Consequently, with \(t=p^{-s}\),

\[
\begin{aligned}
\zeta_{2,2,p}(s)
&=\sum_{\substack{e_i\ge0\\ e_4,e_5\le e_3\\ e_5\le e_4\le e_5+e_1}}
 t^{e_1+2e_2+3e_3}\\
&=\frac{1}{(1-t)(1-t^2)(1-t^3)}
  \sum_{e_4\ge e_5\ge0}t^{4e_4-e_5}\\
&=\frac{1}{(1-t)(1-t^2)(1-t^3)^2(1-t^4)}.
\end{aligned}
\]

For the middle equality, summing over \(e_1\ge e_4-e_5\) contributes \(t^{e_4-e_5}/(1-t)\), summing over \(e_3\ge e_4\) contributes \(t^{3e_4}/(1-t^3)\), and \(e_2\) contributes \(1/(1-t^2)\). Finally,

\[
\sum_{e_4\ge e_5\ge0}t^{4e_4-e_5}=\frac{1}{(1-t^3)(1-t^4)}.
\]

Taking the product over all primes and using \(\prod_p(1-p^{-ks})^{-1}=\zeta(ks)\) gives the stated formula. The summatory asymptotic follows from the simple pole at \(s=1\): its residue is \(\zeta(2)\zeta(3)^2\zeta(4)=\pi^6\zeta(3)^2/540\); the coefficients are nonnegative, so the standard Tauberian conclusion applies.

## Verification

The standalone checker `verify_coefficients.py` independently expands the five geometric factors and verifies the first twenty local coefficients listed in the source. It checks the arithmetic expansion only; it does not certify the infinite double-coset classification. The latter is the proof step described above and is taken from the inspected primary text.

## Relationship to prior work

Du Sautoy’s general framework establishes an Euler product and rationality properties for local zeta functions counting finite nilpotent groups, but that framework alone does not give the explicit factorization here. Voll’s paper states that explicit calculations for nonabelian class-bounded families were largely unavailable and supplies this formula as its main theorem. The result is a special case of the general group-zeta framework, but its uniform local factor \((1-t)^{-1}(1-t^2)^{-1}(1-t^3)^{-2}(1-t^4)^{-1}\) is an explicit evaluation, not merely a rationality assertion.

Semantic searches of the available research-result index for the exact product, aliases \(g(n,2,2)\) and \(\zeta_{2,2}\), and the class-two/two-generator formulation did not return an equivalent or stronger formula. The closest results concerned different invariants of two-generated class-two groups or other nilpotent-group statistics. This search is a bounded overlap check, not a proof that no other publication exists.

## Limitations

The formula applies only to groups of nilpotency class at most two generated by at most two elements. It does not imply analogous prime-uniform products for class three or three generators. The coefficient checker verifies the local factor expansion, not the group-to-ideal correspondence or the uniqueness of the double-coset representatives. Independent audit has not been performed.

## References

1. C. Voll, “Enumerating finite class-2-nilpotent groups on 2 generators,” arXiv:0908.1355, first submitted 10 August 2009; see Theorem 1 and Section 2.
2. M. P. F. du Sautoy, “Counting p-groups and nilpotent groups,” Publications Mathématiques de l’IHÉS 92 (2000), 63–112.
3. F. J. Grunewald, D. Segal, and G. C. Smith, “Subgroups of finite index in nilpotent groups,” Inventiones Mathematicae 93 (1988), 185–223.
