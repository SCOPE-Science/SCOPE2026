# Sharp min–max correlation over three-point probability weights

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let \(X_1,X_2\) be iid with values in the equally spaced set \(\{1,2,3\}\), with
\[
\Pr(X_i=1)=p_1,\qquad \Pr(X_i=2)=p_2,\qquad \Pr(X_i=3)=p_3,
\]
where the law is nondegenerate. Put
\[
M=\min(X_1,X_2),\qquad L=\max(X_1,X_2).
\]
Then
\[
\boxed{\operatorname{Corr}(M,L)\le \frac{8}{19}}.
\]
Equality holds if and only if
\[
p_1=p_2=p_3=\frac13.
\]
Thus, for sample size two and the extreme order-statistic pair on three equally spaced support points, the uniform probability vector is the unique maximizer of Pearson correlation.

If all three probabilities are required to be positive, the complete attainable range is
\[
\boxed{0<\operatorname{Corr}(M,L)\le \frac{8}{19}}.
\]
Every value in this interval is attained. If zero probabilities are admitted while the law remains nondegenerate, the same upper bound and equality characterization remain valid; on each two-point edge the correlation is at most \(1/3\).

## Proof

Correlation is invariant under a common positive affine transformation, so replace \(\{1,2,3\}\) by \(\{-1,0,1\}\). Write
\[
\Pr(X=-1)=x,\qquad \Pr(X=0)=1-q,\qquad \Pr(X=1)=z,
\]
with
\[
q=x+z,\qquad r=z-x,\qquad t=r^2.
\]
For a full-support law, \(0<q<1\) and \(0\le t<q^2\).

Let \(G=\mathbb E|X_1-X_2|\). Direct calculation gives
\[
G=2q-q^2-t,
\qquad
\operatorname{Var}(X)=q-t.
\]
Since \(M+L=X_1+X_2\), \(L-M=|X_1-X_2|\), and \(ML=X_1X_2\),
\[
\operatorname{Cov}(M,L)=\frac{G^2}{4}.
\]
Also
\[
T:=\operatorname{Var}(M)+\operatorname{Var}(L)
=2(q-t)-\frac{G^2}{2},
\]
and
\[
\operatorname{Var}(L)-\operatorname{Var}(M)
=2r\bigl(1-3q+q^2+t\bigr).
\]
Consequently the squared correlation is the rational function
\[
R(q,t):=\operatorname{Corr}(M,L)^2
=
\frac{G^4}{4\left[T^2-4t(1-3q+q^2+t)^2\right]}.
\tag{1}
\]
The denominator is positive whenever the parent law is nondegenerate.

### 1. No nonsymmetric interior maximizer

In the strict region \(0<q<1\), \(0<t<q^2\), exact differentiation of (1) has the form
\[
\frac{\partial R}{\partial t}
\propto 8(q^2-2q+t)^3 P(q,t),
\qquad
\frac{\partial R}{\partial q}
\propto -8(q^2-2q+t)^3 Q(q,t),
\]
where the omitted common denominators are strictly positive. The exact resultant of the two residual polynomials is
\[
\operatorname{Res}_t(P,Q)
=-2304q(q-1)^9(2q-1)(4q^2-2q+1).
\tag{2}
\]
Because \(4q^2-2q+1>0\), an interior common zero could only have \(q=1/2\). At \(q=1/2\),
\[
P=-\frac{(4t-1)(16t^2+8t+17)}{64},
\qquad
Q=\frac{(4t-1)(16t^2-24t-23)}{64},
\]
so their only common real root is \(t=1/4=q^2\), which lies on the boundary rather than in \(0<t<q^2\). Hence no nonsymmetric full-support interior point is stationary.

### 2. The symmetry line

When \(r=0\), so \(t=0\), (1) reduces to
\[
R(q,0)=
\frac{q^2(q-2)^4}{(q^3-4q^2+4q-4)^2}.
\]
Its derivative is
\[
\frac{d}{dq}R(q,0)
=
\frac{-8q(q-2)^3(3q-2)}{(q^3-4q^2+4q-4)^3}.
\]
Thus the unique maximum on \(0<q<1\) occurs at \(q=2/3\), and
\[
R\!\left(\frac23,0\right)=\frac{64}{361}.
\]
The conditions \(q=2/3\) and \(r=0\) are exactly \(x=z=1/3\), hence \(p_1=p_2=p_3=1/3\), and the correlation is \(8/19\).

### 3. Simplex boundaries

If one endpoint probability vanishes, \(t=q^2\), and
\[
R(q,q^2)=\frac{q(1-q)}{(2-q)(1+q)}\le \frac19,
\]
with equality at \(q=1/2\). If the middle probability vanishes, \(q=1\), and
\[
R(1,t)=\frac{1-t}{9-t}\le\frac19,
\]
with equality at \(t=0\). At a point-mass vertex the correlation is undefined, while (1) tends to zero along nondegenerate laws approaching that vertex. Therefore no boundary sequence can exceed the full-support value \(64/361\).

Together with the absence of nonsymmetric interior stationary points, these calculations prove the global bound and its unique equality case.

Finally, along the symmetric family
\[
(p_1,p_2,p_3)=\left(\frac q2,1-q,\frac q2\right),\qquad 0<q\le\frac23,
\]
the displayed derivative is positive until \(q=2/3\), while the correlation tends to zero as \(q\downarrow0\). Continuity therefore gives every value in \((0,8/19]\).

## Literature context and direction of improvement

Terrell (1983) proved that for a sample of size two from a general parent distribution the correlation between the minimum and maximum is at most \(1/2\), with equality characterizing rectangular laws; Székely and Móri (1985) strengthened the surrounding maximal-correlation theory. López-Blázquez and Salamanca-Miño (1999) obtained sharper bounds for discrete distributions on a fixed number of support points.

López-Blázquez and Salamanca-Miño (2021) developed automatic-differentiation methods for order statistics from discrete parents and explicitly included the \(N=3\), \(n=2\), extreme-order-statistic calculation as a computational example. Papadatos (2022; published 2023) then studied the equally weighted discrete analogue and, in its extensions section, fixed a support \(\{1,\ldots,N\}\) while varying its probability vector. After displaying nonuniform \(N=3\) examples, that paper states that the correlation of any two order statistics is expected to be maximized by the uniform probability vector but that no proof was available.

The theorem above supplies a closed sharp proof for the first nontrivial probability-weight case of that conjectural direction: \(N=3\), sample size \(n=2\), and the minimum–maximum pair. The improvement is therefore not a new formula for correlation at a fixed probability vector, but an exact global optimization over the entire probability simplex, including the sharp constant, unique equality case, boundary analysis, and attainable range.

A literature search through the publication date did not identify a later proof of this specific probability-vector maximization. This originality assessment is to the best of our knowledge; terminology and indexing are not exhaustive.

## Limitations

- The result is specific to three equally spaced support points, a sample of size two, and the extreme order-statistic pair.
- It does not prove the probability-vector conjecture for \(N\ge4\), other order-statistic pairs, arbitrary support locations, maximal correlation after nonlinear transformations, or sampling without replacement.
- The 2021 computational paper is very close prior work and already treats the same \(N=3,n=2\) fixed-\(p\) calculation. The claimed contribution here is the exact global maximization and equality/range theorem, not the underlying fixed-\(p\) correlation formula.
- The algebraic elimination step is exact but computer-checkable rather than formally verified in a proof assistant. A compact exact-arithmetic script is included.

## Reproducibility

`artifacts/verify_three_point_minmax.py` reconstructs the direct moments, verifies formula (1), computes the exact derivative resultant (2), checks the \(q=1/2\) boundary root, verifies the symmetry-line and simplex-edge extrema, and checks both the uniform value \(8/19\) and Papadatos's benchmark \(9/23\) for \(p=(1/4,1/2,1/4)\). `artifacts/verification_output.txt` records the exact symbolic checks.

## References

1. G. R. Terrell, “A characterization of rectangular distributions,” *Annals of Probability* 11(3), 823–826 (1983).
2. G. J. Székely and T. F. Móri, “An extremal property of rectangular distributions,” *Statistics & Probability Letters* 3(2), 107–109 (1985). https://doi.org/10.1016/0167-7152(85)90035-5
3. F. López-Blázquez and B. Salamanca-Miño, “On Terrel's characterization of uniform distribution,” *Statistical Papers* 40(3), 335–342 (1999). https://doi.org/10.1007/BF02929879
4. F. López-Blázquez and B. Salamanca-Miño, “Automatic differentiation and maximal correlation of order statistics from discrete parents,” *Computational Statistics* 36, 2889–2915 (2021). https://doi.org/10.1007/s00180-021-01103-5
5. N. Papadatos, “A discrete analogue of Terrell's characterization of rectangular distributions,” arXiv:2205.14360 (2022); *Mathematical Methods of Statistics* 32(2), 122–132 (2023). https://arxiv.org/abs/2205.14360 ; https://doi.org/10.3103/S1066530723020035
