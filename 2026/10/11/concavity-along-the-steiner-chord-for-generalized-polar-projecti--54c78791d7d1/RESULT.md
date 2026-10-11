# Concavity along the Steiner chord for generalized polar projection measures

## Finding
Let \(n\ge2\), \(m\ge1\), and \(p\ge1\). Let \(K\subset\mathbb R^n\) and \(Q\subset\mathbb R^m\) be convex bodies containing the origin in their interiors. Fix \(u\in\mathbb S^{{n-1}}\), and let \(K_u(t)\), \(-1\le t\le1\), be the volume-preserving linear parameter system used for Steiner symmetrization by Marín Sola. Thus \(K_u(1)=K\), \(K_u(-1)=R^uK\), and \(K_u(0)=S^uK\).

Let \(\nu\) be an absolutely continuous rotationally invariant Borel measure on \(\mathbb R^{{nm}}\) whose density is \(\gamma\)-concave, with
\[
\gamma\ge-\frac1{{nm}}.
\]
Define
\[
A_\nu(t)=\nu\!\left(\Pi^\circ_{{Q,p}}(K_u(t))\right).
\]
Then \(A_\nu\) is even and \(s_\gamma\)-concave on \([-1,1]\), where
\[
s_\gamma=\frac{{\gamma}}{{1+nm\gamma}}.
\]
At the lower endpoint \(\gamma=-1/(nm)\), interpret \(s_\gamma=-\infty\); at \(\gamma=0\), interpret \(s_0=0\); and for \(\gamma=\infty\), use the limit \(s_\infty=1/(nm)\). Thus for all \(t_0,t_1\in[-1,1]\) and \(0\le\lambda\le1\),
\[
A_\nu((1-\lambda)t_0+\lambda t_1)
\ge
M_{{s_\gamma}}\!\left(A_\nu(t_0),A_\nu(t_1);\lambda\right),
\]
where \(M_s\) is the weighted power mean with the usual logarithmic and endpoint conventions.

Since \(A_\nu\) is even, this immediately yields
\[
0\le s\le t\le1
\quad\Longrightarrow\quad
A_\nu(t)\le A_\nu(s).
\]
Hence the endpoint Steiner comparison belongs to a full one-parameter concavity law.

For Lebesgue measure, the density is \(\infty\)-concave on its convex support, so
\[
t\longmapsto
\left|\Pi^\circ_{{Q,p}}(K_u(t))\right|^{{1/(nm)}}
\]
is even and concave. More generally, for every \(R>0\), the density of Lebesgue measure restricted to \(R B_2^{{nm}}\) is constant on a convex rotationally invariant support, and therefore
\[
t\longmapsto
\left|\Pi^\circ_{{Q,p}}(K_u(t))\cap R B_2^{{nm}}\right|^{{1/(nm)}}
\]
is even and concave. Thus every centered-ball truncation profile satisfies a Brunn--Minkowski-strength interpolation law, not merely endpoint monotonicity.

## Assumptions and scope
The generalized polar projection body is the \((L_p,Q)\) operator characterized by
\[
\|x\|_{{\Pi^\circ_{{Q,p}}K}}^p=nV_p(K,xQ^t).
\]
The density concavity is understood on its convex support, as in the Borell--Brascamp--Lieb framework. This matters for positive \(\gamma\): a compactly supported density need not remain \(\gamma\)-concave after an arbitrary zero extension, while the support-based formulation is exactly what the marginal theorem uses.

No strict concavity, equality classification, or set inclusion is asserted. The theorem concerns the specific Steiner linear parameter system \(K_u(t)\) used in the lead source, rather than every possible continuous symmetrization flow.

## Proof
Marín Sola's proof of the measure-valued \((L_p,Q)\) Petty inequality writes the measure of the generalized polar projection body as a marginal over the variables used to split \(\mathbb R^{{nm}}\) relative to \(u\). In those coordinates, write \(z=(y,\bar s)\in\mathbb R^{{nm}}\). The proof identifies a set
\[
\mathcal C=\{{(t,z): f_p(t,z)\le1}\}
\subset[-1,1]\times\mathbb R^{{nm}}
\]
whose convexity follows from the joint convexity of the relevant \(L_p\) mixed-volume gauge. If \(\phi\) is the density of \(\nu\), then
\[
A_\nu(t)
=
\int_{{\mathbb R^{{nm}}}}
\mathbf 1_{{\mathcal C}}(t,z)\,\phi(z)\,dz.
\]
The source uses this structure at the limiting exponent \(-1/(nm)\) to prove the Steiner endpoint inequality. Retaining the actual density exponent gives more.

Because \(\mathcal C\) is convex and \(\phi\) is \(\gamma\)-concave on its convex support, the joint density \((t,z)\mapsto\mathbf 1_{{\mathcal C}}(t,z)\phi(z)\) is \(\gamma\)-concave on its convex support. The Borell--Brascamp--Lieb marginal theorem in dimension \(nm\) therefore gives \(s_\gamma\)-concavity of its marginal in \(t\), with
\[
s_\gamma=rac{{\gamma}}{{1+nm\gamma}}.
\]
The assumption \(\gamma\ge-1/(nm)\) is exactly the admissible range for this marginalization. The critical value gives the quasi-concave endpoint \(s_\gamma=-\infty\); \(\gamma=0\) gives log-concavity; and \(\gamma=\infty\) gives \(1/(nm)\)-concavity.

The same reflection argument in the lead proof gives
\[
A_\nu(-t)=A_\nu(t),
\]
because \(K_u(-t)\) is the reflected member of the Steiner chord and \(\nu\) is rotationally invariant. This proves evenness.

For the monotonicity consequence, fix \(0\le s\le t\le1\). If \(t>0\), then
\[
s=(1-\lambda)(-t)+\lambda t,
\qquad
\lambda=\frac{1+s/t}{2}.
\]
Applying \(s_\gamma\)-concavity and evenness gives
\[
A_\nu(s)
\ge
M_{{s_\gamma}}(A_\nu(-t),A_\nu(t);\lambda)
=A_\nu(t).
\]
The case \(t=0\) is immediate.

Finally, Lebesgue measure has constant density on \(\mathbb R^{{nm}}\), and restricted Lebesgue measure on \(R B_2^{{nm}}\) has constant density on a convex support. Both correspond to \(\gamma=\infty\), so \(s_\infty=1/(nm)\), proving the two root-concavity statements.

## Verification
The claim was checked against the actual proof architecture of the lead source, not inferred from its endpoint theorem alone. The relevant source steps are: the volume-preserving Steiner linear parameter system; the disintegration of \(\nu(\Pi^\circ_{{Q,p}}(K_u(t)))\); convexity of the mixed-volume gauge that makes the joint admissible set convex; application of the Borell--Brascamp--Lieb marginal principle at the critical density exponent; and the reflection identity producing evenness. The new step is to keep the actual \(\gamma\)-concavity exponent through the same marginalization instead of lowering it to the critical value \(-1/(nm)\).

The exponent transformation was checked directly: marginalizing a \(\gamma\)-concave density over \(d=nm\) variables gives \(\gamma/(1+d\gamma)\). Its limits agree with the standard cases: \(\gamma=0\) gives log-concavity, \(\gamma\downarrow-1/d\) gives the quasi-concave endpoint, and \(\gamma\to\infty\) gives the Brunn--Minkowski exponent \(1/d\). No finite experiment or numerical approximation is used to prove the universal statement.

## Relationship to prior work
F. Marín Sola, arXiv:2503.00949 / DOI:10.1112/blms.70187, proves the generalized Petty projection inequality for rotationally invariant measures with \(\gamma\)-concave density for \(\gamma\ge-1/(nm)\). Its Steiner proof contains the convex joint support, marginalization, and evenness used above, but the stated theorem is the endpoint comparison with the Steiner symmetral. The concavity law in the interpolation parameter is not stated there.

Y. Lin, arXiv:2102.07103, proves a classical endpoint Petty-projection comparison under Steiner symmetrization in the finite-perimeter setting. That theorem does not imply the present \((L_p,Q)\), measure-valued interpolation law.

Brunn--Minkowski inequalities for polar projection bodies under Minkowski addition, including DOI:10.1007/s12220-026-02365-5 and earlier additive-map results, concern a different deformation of the input body. They do not imply concavity along the Steiner linear parameter system considered here.

Targeted searches for Steiner-parameter concavity, shadow-system formulations, \((L_p,Q)\) aliases, and root-concavity of polar projection volumes found no checked statement implying the theorem above.

## Limitations
The result does not classify equality or prove strict concavity away from bodies already symmetric about \(u^\perp\). It does not assert inclusion between \(\Pi^\circ_{{Q,p}}(K_u(t))\) for different parameters. It also does not replace the full global Petty inequality: it describes only the one-dimensional Steiner interpolation used in that proof.

The originality assessment is literature-based rather than exhaustive over all historical terminology. A differently named shadow-system formulation not captured by the checked sources remains a residual risk.

## References
1. F. Marín Sola, *On general versions of the Petty projection inequality*, arXiv:2503.00949; DOI:10.1112/blms.70187.
2. Y. Lin, *The Petty projection inequality for sets of finite perimeter*, arXiv:2102.07103.
3. C. Borell, *Convex set functions in \(d\)-space*, Period. Math. Hungar. 6 (1975), 111--136.
4. H. J. Brascamp and E. H. Lieb, *On extensions of the Brunn--Minkowski and Prékopa--Leindler theorems*, J. Funct. Anal. 22 (1976), 366--389.
5. D. Zou, W. Li, and D. Li, *The Brunn--Minkowski inequality for the polar projection body*, J. Geom. Anal. 36 (2026), Article 121; DOI:10.1007/s12220-026-02365-5.
