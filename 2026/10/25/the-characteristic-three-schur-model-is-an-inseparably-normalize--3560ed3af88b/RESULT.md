# The characteristic-three Schur model is an inseparably normalized quartic scroll

## Finding

Let \(k\) be any field of characteristic \(3\). Reduce the *displayed integral equation* of Schur's quartic,
\[
X^4-XY^3=W^4-WZ^3,
\]
in \(\mathbf P^3_k\). The resulting surface \(S\) is geometrically integral and nonnormal, with reduced singular locus a line and scheme-theoretic generic transverse singular length \(9\). Its normalization is the Hirzebruch surface \(\mathbb F_2\), and the normalization map is a finite universal homeomorphism that restricts to the relative cubing map on the preimage of the singular line.

Every geometric line on \(S\) is one of its two distinguished directrices or belongs to one ruling indexed by \(\mathbf P^1\). For every \(q=3^m\), with integer \(m\ge1\), there are exactly \(q+3\) lines defined over \(\mathbb F_q\), and
\[
\#S(\mathbb F_q)=(q+1)^2,\qquad
Z(S/\mathbb F_q,T)=\frac1{(1-T)(1-qT)^2(1-q^2T)}.
\]
This concerns the literal displayed integral model only; it is *not* the different, smooth characteristic-three model of the Schur K3 surface known to be isomorphic to a Fermat quartic.

## Assumptions and scope

Use homogeneous coordinates \([X:Y:W:Z]\) on \(\mathbf P^3_k\). Put \(a=X-Y\), \(b=W-Z\), \(u=X\), and \(v=W\). This is a projective linear coordinate change over \(k\), in which the characteristic-three equation is
\[
S:\quad ua^3-vb^3=0\quad\text{in }\mathbf P^3_{[a:b:u:v]}.
\]
Define the singular directrix \(L=\{a=b=0\}\), the other directrix \(L_0=\{u=v=0\}\), and for each geometric point \([s:t]\in\mathbf P^1(\bar k)\) the line
\[
\ell_{[s:t]}=\left\langle[s:t:0:0],\ [0:0:t^3:s^3]\right\rangle.
\]
A line over \(\mathbb F_q\) means a geometric projective line stable under \(q\)-Frobenius; this is stronger than the condition that the defining quartic vanish at the finitely many rational points of an arbitrary candidate line.

## Proof

**Integral surface and singular scheme.** The polynomial \(ua^3-vb^3\) is primitive and linear in \(u,v\), and \(a^3\), \(b^3\) are relatively prime. Gauss's lemma makes it irreducible after every extension of \(k\), proving geometric integrality. Its four partial derivatives in characteristic \(3\), in the coordinate order \((a,b,u,v)\), are \((0,0,a^3,-b^3)\). Thus the Jacobian singular subscheme has homogeneous ideal \((a^3,b^3)\) *on* \(S\), with reduced support \(L\). At the generic point of \(L\), the transverse artinian intersection is defined by \((a^3,b^3)\) and has length \(3\cdot3=9\). Because the singular set has codimension one in the geometrically integral hypersurface, Serre's normality criterion shows that \(S\) is nonnormal.

**Normalization and the inseparable directrix.** In \(\mathbf P^1_{[s:t]}\times\mathbf P^3\), form the incidence surface
\[
I:\quad ta-sb=0,\qquad s^3u-t^3v=0.
\]
For each \([s:t]\), these two independent linear equations leave a projective line, namely \(\ell_{[s:t]}\). The respective kernels in the \((a,b)\)-plane and \((u,v)\)-plane are \(\mathcal O_{\mathbf P^1}(-1)\) and \(\mathcal O_{\mathbf P^1}(-3)\). Therefore
\[
I\simeq\mathbf P_{\mathbf P^1}\bigl(\mathcal O(-1)\oplus\mathcal O(-3)\bigr)\simeq\mathbb F_2.
\]
Projection \(\nu:I\to\mathbf P^3\) has image in \(S\). Outside \(L\) one uniquely reconstructs \([s:t]=[a:b]\), making \(\nu\) an isomorphism there. Above \(L\), the points satisfy \(a=b=0\) and \([u:v]=[t^3:s^3]\), so the restriction is the cubic Frobenius map of projective lines after swapping coordinates. Each geometric fiber has one point; hence the projective morphism is proper and quasi-finite, therefore finite. Being finite, birational, with smooth normal source, it is the normalization of \(S\); the fiber description also makes it radicial and surjective, hence a universal homeomorphism. Its map on \(L\) is purely inseparable of degree \(3\).

**Exhaustion of geometric lines.** Let \(M\subset S_{\bar k}\) be any projective line. Examine the two restrictions of \(a,b\) as degree-one forms on \(M\). If both vanish, \(M=L\). If they span a one-dimensional space, write \((a,b)=h(s,t)\) with fixed \([s:t]\); the equation forces the restrictions of \(u,v\) to satisfy \(s^3u=t^3v\). Thus \(M=\ell_{[s:t]}\). If they are independent, use them as homogeneous coordinates \((s,t)\) on \(M\); write \(u=\alpha s+\beta t\) and \(v=\gamma s+\delta t\). The identity
\[
\alpha s^4+\beta s^3t-\gamma st^3-\delta t^4\equiv0
\]
forces all four coefficients to vanish, whence \(M=L_0\). These cases are exhaustive and the listed lines are distinct. The ruling assignment \([s:t]\mapsto\ell_{[s:t]}\) is defined over \(\mathbb F_3\) and injective; therefore \(\ell_{[s:t]}\) descends to \(\mathbb F_q\) exactly when \([s:t]\in\mathbf P^1(\mathbb F_q)\). Including the two directrices gives \(q+3\) rational lines.

**Point counting and zeta function.** For any finite field \(\mathbb F_q\) in characteristic \(3\), the normalization induces a bijection on \(\mathbb F_q\)-points. Away from \(L\) it is an isomorphism; along \(L\) it is Frobenius cubing, which is a bijection on every finite field. The projective bundle \(I\to\mathbf P^1\) has \(q+1\) rational lines as fibers, each with \(q+1\) rational points. Thus \(\#S(\mathbb F_q)=(q+1)^2\), and the same statement over all extensions gives the displayed zeta function by the exponential definition \(Z=\exp(\sum_{r\ge1}\#S(\mathbb F_{q^r})T^r/r)\).

## Verification

The standalone, standard-library-only file `verify.py` implements exact field arithmetic for \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\); it enumerates projective points and checks the predicted counts \(16,100,784\), and checks the singular line points. It also enumerates all rational two-dimensional subspaces of \(\mathbb F_q^4\) for \(q=3,9\), testing identically zero quartic *restrictions*, finding exactly \(6\) and \(12\) defined lines. It deliberately distinguishes polynomial vanishing from mere pointwise tests in \(\mathbb F_3\), where the latter produces two false positives. A successful local run printed `VERIFY_OK`. The geometric arguments above, rather than the finite enumerations, prove the statements for all fields of characteristic \(3\).

## Relationship to prior work

Veniani's 2017 article treats complex smooth quartics, their configurations of lines and explicit equations, including Schur's surface. Rams and Schütt (2012/2015) give Schur's equation and explicitly note a *good reduction model* in characteristic \(3\) isomorphic to the Fermat quartic. This does not imply claims about the distinct **literal equation reduced coefficientwise**: the latter is the nonnormal scroll studied here, whereas a smooth K3 quartic cannot have a singular line or the ruled normalization \(\mathbb F_2\). González-Alonso and Rams (2015) survey complex ruled quartic surfaces and line bounds; that work does not identify this inseparable characteristic-three special fiber or determine its Frobenius and point counts. The full named statements are compared, not only keyword/title matches. No equivalent statement was identified in the accessible literature and mathematical-record searches. This is a best-knowledge originality assessment, not a proof of universal priority.

## Limitations

The construction applies to the literal equation \(X^4-XY^3=W^4-WZ^3\) in characteristic \(3\), rather than to arbitrary integral models of the Schur K3 surface, arbitrary quartic surfaces or good characteristic-three K3 reductions. It describes geometric/projective lines and rational points, but does not classify all nonreduced structure of the Hilbert scheme of lines. The finite computations check small fields only; the uniform conclusions follow independently from the proofs. Possible unindexed historical treatments of inseparable ruled quartic models are a residual originality risk.

## References

- D. C. Veniani, *Symmetries and equations of smooth quartic surfaces with many lines*, first submitted 2017-08-03, arXiv:1708.01219; https://arxiv.org/abs/1708.01219.
- S. Rams and M. Schütt, *64 lines on smooth quartic surfaces*, first submitted 2012-12-14, arXiv:1212.3511; https://arxiv.org/abs/1212.3511. Especially the distinction concerning a good characteristic-three model in the introduction.
- V. González-Alonso and S. Rams, *Counting Lines on Quartic Surfaces*, first submitted 2015-05-08, arXiv:1505.02018; https://arxiv.org/abs/1505.02018.
