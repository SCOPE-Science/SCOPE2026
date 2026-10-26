# Dyadic extinction and sharp transient laws for triangular-torus parity dynamics

## Finding

Consider the synchronous six-neighbour binary parity rule on a triangular torus. For all integers \(m,n\geq3\), write \(m=kr\), \(n=\ell s\), where \(k,\ell\) are powers of two and \(r,s\) are odd, and put \(g=\gcd(r,s)\). Its space of recurrent configurations has exactly \(2^d\) points, where
\[
d=k\ell\bigl((r-1)(s-1)-(g-1)\bigr).
\]
Every recurrent phase has exactly \(2^{mn-d}\) initial configurations mapping to it after the uniform convergence time \(T\) below. The **exact largest transient length**, measured as the number of updates before the orbit first enters its eventual periodic cycle, is
\[
T=\begin{cases}
\max(1,k/2),&r=s=1,\ k=\ell,\\
\min(k,\ell),&r=s=1,\ k\ne\ell,\\
k,&r=1,\ s>1,\\
\ell,&s=1,\ r>1,\\
\max(k,\ell),&r>1,\ s>1.
\end{cases}
\]
(The first branch includes the formally degenerate case \(k=\ell=1\), although the stipulated circumferences exclude it.) Global extinction—every state ultimately becoming all zero—occurs **exactly when at least one circumference is a power of two**.

Two further exact last-step laws hold for power-of-two circumferences. On a square torus \(m=n=2h\) with \(h\ge2\) a power of two, the rank of the penultimate iterate is \(3h\), so the fraction of states requiring the full \(h\) updates to vanish is \(1-2^{-3h}\). On a rectangular torus \(m\) by \(n\) with \(m,n\) powers of two and \(n\ge2m\), the sharp extinction time is \(m\) and the fraction needing every update is \(1-2^{-(n-2m+2)}\). All counts refer to *labelled* vertex configurations.

## Assumptions and scope

The vertex set is \((\mathbb Z/m\mathbb Z)\times(\mathbb Z/n\mathbb Z)\). The six distinct neighbours of \((i,j)\), for \(m,n\ge3\), are \((i\pm1,j)\), \((i,j\pm1)\), and \((i\pm1,j\pm1)\) with matching signs on the two coordinates (namely \((i+1,j+1)\), \((i-1,j-1)\)). A binary state belongs to the vector space \(\mathbb F_2^{mn}\); its next state at each vertex is the sum modulo two of these six neighbours' bits, without a self-loop. All updates occur synchronously. A recurrent state lies on a finite periodic orbit; its transient length is the first time it is periodic. The largest such length over all initial configurations is \(T\). When \(F^T\) maps to a recurrent phase, an attraction fibre means \((F^T)^{-1}\) of that *phase*, not the union of phases in a cycle.

## Proof

**1. Convolution factorization.** In the group algebra
\[
\mathcal R_{m,n}=\mathbb F_2[x^{\pm1},y^{\pm1}]/(x^m-1,y^n-1),
\]
updates are multiplication by
\[
A=x+x^{-1}+y+y^{-1}+xy+x^{-1}y^{-1}
  =(xy)^{-1}(x+1)(y+1)(xy+1).
\]
The second identity follows by expanding the three factors over characteristic two; it is specific to the six-neighbour diagonal orientation chosen above. Multiplication by \((xy)^{-1}\) is invertible in every factor and therefore never affects ranks, recurrent subspaces or nilpotency indices.

**2. Semisimple roots and the recurrent dimension.** Let \(K\) be an algebraic closure of \(\mathbb F_2\). Because \(r,s\) are odd and \(k,\ell\) powers of two, the Chinese remainder decomposition gives
\[
K\otimes\mathcal R_{m,n}\cong
\prod_{\xi^r=1,\,\eta^s=1} K[u,v]/(u^k,v^\ell),
\]
with \(x=\xi(1+u)\) and \(y=\eta(1+v)\). In a local factor, \(A\) is a unit if and only if \(\xi\ne1\), \(\eta\ne1\), and \(\xi\eta\ne1\); otherwise it is nilpotent. The three excluded root sets respectively have \(s\), \(r\), and \(g=\gcd(r,s)\) points, and their pairwise and triple intersections are all the single point \((1,1)\). Inclusion–exclusion leaves
\[
rs-(s+r+g-2)=(r-1)(s-1)-(g-1)
\]
unit factors. Each factor has dimension \(k\ell\) over \(K\), hence their direct sum has dimension \(d\). Scalar extension preserves matrix ranks; the recurrent space over \(\mathbb F_2\) consequently also has dimension \(d\). For sufficiently large \(t\), multiplication by \(A^t\) vanishes precisely on the nilpotent factors and is invertible on all unit factors. Thus \(\operatorname{im}(F^t)\) is exactly the recurrent subspace, and each of its \(2^d\) states has \(2^{mn-d}\) preimages.

**3. Sharp local nilpotency indices.** On a factor with \(\xi=1\), \(\eta\ne1\), the symbol is a unit times \(u\), of exact nilpotency index \(k\). The symmetric factors have index \(\ell\). Where \(\xi\eta=1\) and neither root is one, it is a unit times
\[
w=u+v+uv=u+v(1+u).
\]
The map \(v\mapsto v(1+u)\) is an automorphism of \(K[u,v]/(u^k,v^\ell)\), so the index equals that of \(u+v\), namely \(\max(k,\ell)\): Frobenius annihilates at that power, whereas the immediately previous power has a nonzero extreme monomial.

At the central factor \((\xi,\eta)=(1,1)\), the symbol is a unit times \(u v w\). If \(k<\ell\), the index is \(k\). Indeed \((uvw)^k=0\), while in \((uvw)^{k-1}\) the term \(u^{k-1}v^{2k-2}\) occurs with coefficient one and has no competing contribution, since \(2k-2<\ell\). Its symmetric counterpart gives index \(\ell\) if \(\ell<k\). When \(k=\ell=2h\ge4\), Frobenius gives
\[
(uvw)^h=u^h v^h(u^h+v^h+u^h v^h)=0,
\]
and \((uvw)^{h-1}\) has a nonzero monomial \(u^{2h-2}v^{h-1}\) coming uniquely from the \(u^{h-1}\) term of \(w^{h-1}\). Thus the index is exactly \(h\). If \(k=\ell=1\), the factor is one-dimensional and the symbol vanishes, so its index is one.

Combining local indices gives \(T\). If both odd parts exceed one, the distinct factors \((1,\eta\ne1)\) and \((\xi\ne1,1)\) force indices \(k\) and \(\ell\); they dominate every other local index. If exactly one odd part is one, the surviving noncentral zero factors force the corresponding pure power-of-two index. If both are one, only the central factor remains, with the indices just calculated. The maximum nilpotency index is precisely the largest transient length: \(F^{T}\) kills its nilpotent primary part and \(F^{T-1}\) does not. This also proves the exact extinction criterion, since \(d=0\) precisely when \(r=1\) or \(s=1\).

**4. Sharp last-step proportion for dyadic squares.** Set \(m=n=2h\), \(h\ge2\) a power of two, and write \(t=h-1\). The rank of multiplication by \(A^t\) on \(R=\mathbb F_2[u,v]/(u^{2h},v^{2h})\) equals the rank of multiplication by \(w^t\) on
\[
R'=\mathbb F_2[u,v]/(u^{h+1},v^{h+1}),
\]
because multiplying first by \(u^t v^t\) identifies this quotient with the subspace where both exponents are at least \(t\). The unit factors of \(A\) are irrelevant to rank. The automorphism \(v\mapsto v(1+u)\) replaces \(w\) by \(z=u+v\). In coordinates \(u,z\), the relations for \(R'\) are \(u^{h+1}=0\) and
\[
(u+z)^{h+1}=z^{h+1}+uz^h+u^h z+u^{h+1}=0.
\]
After adding \(z^{h-1}=0\), only the extra relation \(u^h z=0\) survives. Hence the quotient by the ideal \((z^{h-1})\) has dimension
\[
(h+1)+h(h-2)=h^2-h+1.
\]
Since \(\dim R'=(h+1)^2\), the ideal generated by \(z^{h-1}\), hence \(\operatorname{im}(F^{h-1})\), has dimension \(3h\). As \(F^h=0\), the proportion of initial states not yet zero at time \(h-1\), and thus of those requiring exactly \(h\) updates, is \(1-2^{-3h}\).

**5. Dyadic rectangles.** Let \(m,n\) be powers of two with \(n\ge2m\), and take \(t=m-1\). Expanding \(u^t v^t w^t\) over \(\mathbb F_2\), every term except \(u^{m-1}v^{2m-2}\) vanishes modulo \(u^m\). Thus \(F^{m-1}\) has exactly \(n-2m+2\) linearly independent output coordinates in the principal ideal and consequently that rank. Since \(F^m=0\), the proportion requiring the full \(m\) updates is \(1-2^{-(n-2m+2)}\). Interchanging the two coordinates gives the symmetric statement.

## Verification

The bundled standalone `triangular_verify.py` constructs the six-neighbour update directly, independently computes powers of its periodic convolution kernel, and calculates exact ranks via binary Gaussian elimination. It checks all 256 ordered size pairs with \(3\le m,n\le18\), verifying \(\operatorname{rank}F^T=d\) and \(\operatorname{rank}F^{T-1}>d\) in every case; it also checks 102,912 labelled-state trajectories in seven small graph sizes and nine dyadic last-step rank predictions. The accompanying output is a reproducible execution record. These finite tests corroborate, but do not replace, the all-size polynomial proof above. Run with a standard Python 3 interpreter: `python triangular_verify.py`.

## Relationship to prior work

Zaidenberg's characteristic-prime lattice-convolution framework develops the general spectral and group-algebra methods for periodic solutions, including two-dimensional neighbourhood operators. The present theorem concerns the *specific* factorable six-neighbour triangular-torus symbol and supplies its all-size recurrent dimension, **exact** nilpotent depth, and last-step ranks; the general framework itself is not an explicit statement of these formulas. Uguz, Siap, and Akin treat hexagonal lattice automata under periodic boundaries, but their inspected 2013 full text studies ternary-field matrix reversibility, not the characteristic-two six-neighbour triangular-torus dynamics here. The inspected 2025 Moore-neighbour triangular-lattice work employs ternary states, a larger neighbourhood, and null boundaries. These distinctions concern actual operators and hypotheses, not just titles. The related 2011 hexagonal-automata paper was identified, but its full text could not be inspected; it remains a historical-overlap risk.

## Limitations

The exact full distribution of every intermediate transient depth and every primitive period is not claimed. The theorem gives the *total* recurrent count, sharp uniform transient, phase-fibre cardinality, and stated final-step distributions. The finite verifier cannot certify the infinite family without the written algebraic argument. Historical originality is supported only relative to inspected literature; an unindexed or inaccessible equivalent result is possible. No independent external audit is claimed.

## References

1. M. G. Zaidenberg, *Convolution equations on lattices: periodic solutions with values in a prime characteristic field*, arXiv:math-ph/0606070v1 (2006). https://arxiv.org/abs/math-ph/0606070
2. S. Uguz, I. Siap, H. Akin, *2-Dimensional Reversible Hexagonal Cellular Automata with Periodic Boundary*, Acta Physica Polonica A **123** (2013), 480–483. https://doi.org/10.12693/APhysPolA.123.480
3. I. Siap, H. Akin, S. Uguz, *Structure and reversibility of 2D hexagonal cellular automata* (2011). https://doi.org/10.1016/j.camwa.2011.09.066
4. Bhavadharani and Christy, *Algebraic Structure of Moore Cellular Automata - Finite Triangular Lattice* (2025). https://doi.org/10.18280/mmep.120726
