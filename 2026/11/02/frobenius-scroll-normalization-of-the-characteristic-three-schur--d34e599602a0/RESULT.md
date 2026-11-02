# Frobenius-scroll normalization of the characteristic-three Schur quartic model

## Finding
Let \(k\) be any field of characteristic \(3\). Let \(S_k\subset\mathbb P^3_k\) be the quartic defined by the reduction of the displayed integral Schur equation
\[
x_0^4-x_0x_1^3-x_2^4+x_2x_3^3=0.
\]
Put \(u=x_0\), \(v=x_2\), \(a=x_0-x_1\), and \(b=x_2-x_3\). Then \(S_k\) is the integral, geometrically integral surface \(ua^3-vb^3=0\), and the following statements hold.

1. Its singular subscheme is \(V(a^3,b^3)\); its reduced singular locus is the line \(L=V(a,b)\). Its normalization is \(\mathbb F_2\cong\mathbb P_{\mathbb P^1}(\mathcal O(3)\oplus\mathcal O(1))\), and the normalization map is finite, birational, and a universal homeomorphism. Along the normalization section over \(L\), the induced map onto \(L\) is the degree-three Frobenius morphism followed by a coordinate interchange.
2. The conductor ideal on \(S_k\) is \(\mathcal I_L^2=(a,b)^2\) as an ideal sheaf, while its pullback to the normalization is the square of the ideal of the inverse-image section of \(L\).
3. Over an algebraic closure, **all** lines on \(S_k\) are \(L\), the skew line \(T=V(u,v)\), and the one-parameter family \(\{\ell_{[s:t]}\}_{[s:t]\in\mathbb P^1}\), where
\[
\ell_{[s:t]}=\overline{[t^3:s^3:0:0]\,[0:0:s:t]}.
\]
The ruling lines are pairwise disjoint; each meets both \(L\) and \(T\), and the two directrices are skew.
4. For each \(q=3^m\), \(m\ge1\), there are exactly \(q+3\) lines defined over \(\mathbb F_q\), and
\[
\#S_k(\mathbb F_q)=(q+1)^2 \quad\text{when }k=\mathbb F_q.
\]
For the model over \(\mathbb F_3\), its Hasse–Weil zeta function is
\[
Z(S_{\mathbb F_3},T)=\frac1{(1-T)(1-3T)^2(1-9T)}.
\]

## Assumptions and scope
The assertion concerns the **specific integral projective equation displayed above**, reduced coefficientwise modulo \(3\). In particular, it does not concern every integral model of the complex Schur quartic. All scheme calculations hold over an arbitrary field \(k\) of characteristic \(3\); the classification of geometric lines is after algebraic closure. All finite-field counts refer to the exact field \(\mathbb F_{3^m}\), not to estimates from sampled degrees.

## Proof
**The reduced equation and singular scheme.** In characteristic \(3\), the identity \((r-s)^3=r^3-s^3\) changes the equation into \(F=ua^3-vb^3\). The partial derivatives in the independent variables \(u,v,a,b\) are \((a^3,-b^3,0,0)\). Because \(F\in(a^3,b^3)\), the Jacobian singular subscheme is exactly \(V(a^3,b^3)\), with reduced support \(L=V(a,b)\). On the chart \(v\ne0\), setting \(v=1\) gives the domain
\[
R=k[u,a,b]/(b^3-ua^3).
\]
This is a domain: over \(k(u)\), the element \(u\) is not a cube, so \(b^3-ua^3\) is irreducible. The same argument after extending the constant field proves geometric integrality.

**Normalization.** Use the quotient convention for the projective bundle \(N=\mathbb P_{\mathbb P^1}(\mathcal O(3)\oplus\mathcal O(1))\cong\mathbb F_2\). The four base-point-free sections \((t^3,s^3;s,t)\) define
\[
\nu:N\longrightarrow\mathbb P^3,
\qquad([s:t],[\lambda:\mu])\longmapsto
[\lambda t^3:\lambda s^3:\mu s:\mu t],
\]
where \([\lambda:\mu]\) denotes a local representative of a quotient in a trivialization of the two summands. Its image satisfies \(ua^3=vb^3\). On \(S_k\setminus L\), \([s:t]=[a:b]\), so \(\nu\) has a regular inverse and is an isomorphism there. The inverse image of \(L\) is the section \(\mu=0\), which maps by \([s:t]\mapsto[t^3:s^3]\) onto \(L\); it has one geometric preimage over every geometric point. Thus \(\nu\) is proper and quasi-finite, hence finite, and it is birational. Its source is smooth and normal, so it is the normalization. Off \(L\) it is an isomorphism; on \(L\) the map is purely inseparable Frobenius. Hence \(\nu\) is also radicial and therefore a universal homeomorphism.

**Conductor.** On \(v=1\), the normalization has the coordinate ring
\[
B=k[t,z],\qquad R=k[t^3,z,tz]\subset B,
\]
under \(u=t^3\), \(a=z\), \(b=tz\). These identities also prove directly that \(B=R[t]\) is finite and birational over \(R\). A monomial \(t^i z^j\) belongs to \(R\) precisely when \(j\ge i\bmod3\), where the residue is in \(\{0,1,2\}\). Therefore \(rB\subset R\) precisely for the \(R\)-linear combinations of monomials with \(j\ge2\). The conductor is
\[
(R:B)=z^2B=(z^2,z(tz),(tz)^2)R=(a^2,ab,b^2)R.
\]
The symmetrical calculation in the chart \(u=1\), and the fact that the map is an isomorphism away from \(L\), identify its global conductor with \(\mathcal I_L^2\). In \(B\), it becomes \(z^2B\), the double of the inverse-image section.

**Classification of lines.** The lines \(L\), \(T=V(u,v)\), and the stated \(\ell_{[s:t]}\) lie on the surface. Let \(D\) be any other geometric line. The pairs \((a,b)\) and \((u,v)\) each restrict to nonzero pairs of linear forms on \(D\cong\mathbb P^1\). They define rational maps \(\alpha:D\dashrightarrow\mathbb P^1\) and \(\beta:D\dashrightarrow\mathbb P^1\) of degree either \(0\) or \(1\). The quartic relation implies \(\beta=[b^3:a^3]\), so if \(\alpha\) were nonconstant then \(\beta\) would have degree \(3\), a contradiction. Hence \(\alpha\) is constant and \(\beta\) is constant, and \(D\) is the line joining the corresponding points of \(T\) and \(L\), namely one \(\ell_{[s:t]}\). Distinct ruling parameters give distinct points on each directrix, making their ruling lines pairwise skew. Every ruling line meets each directrix once. The directrices themselves are skew.

**Finite-field points and zeta function.** Over \(\mathbb F_q\), the two directrices each contain \(q+1\) points. The Frobenius permutation of \(\mathbb P^1(\mathbb F_q)\) makes exactly \(q+1\) ruling lines rational. Each has \(q-1\) additional points off the two directrices, and these sets are disjoint. Thus
\[
\#S_k(\mathbb F_q)=2(q+1)+(q+1)(q-1)=(q+1)^2.
\]
The line classification similarly yields \(q+3\) rational lines. The defining exponential series \(\exp(\sum_{m\ge1}\#S(\mathbb F_{3^m})T^m/m)\) gives the displayed zeta function.

## Verification
Run `python verify.py` from the directory containing this document. It checks the characteristic-three coordinate transformation and Jacobian, the monomial conductor membership pattern in a bounded range, and independently enumerates all projective points over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). The resulting counts are \(16\), \(100\), and \(784\), respectively. The general normalization, conductor, line classification, and all-extension formulas are proved above, not inferred from the bounded tests.

## Relationship to prior work
Rams and Schütt (arXiv:1212.3511; first public 2012-12-14) give the classical displayed Schur equation and its 64-line property outside characteristics \(2,3\). They explicitly distinguish a **suitable model with good reduction** in characteristic \(3\), rather than claiming that the displayed coefficientwise reduction is smooth. Their later characteristic-three paper (arXiv:1409.7485; first public 2014-09-26, especially Remark 4.4) identifies the smooth good-reduction model with the Fermat quartic. The present result instead describes the nonnormal reduction of the displayed naive equation, including its exact conductor and all geometric lines. General Frobenius and ruled-surface methods underlie the proof; no claim is made that those methods are new.

## Limitations
This is a statement about one projective integral model, not a new classification of quartic K3 surfaces, not a determination of the stable reduction of a K3 surface, and not an assertion that all integral models have this special fiber. The reduced geometric line set is classified, but a scheme-theoretic determination of the relative Fano scheme of lines is not claimed. Historical priority is subject to the possibility of earlier computations using equivalent scroll or Frobenius equations.

## References
1. S. Rams and M. Schütt, *64 lines on smooth quartic surfaces*, first public 2012-12-14, arXiv:1212.3511, especially the introduction and equation (1), https://arxiv.org/abs/1212.3511.
2. S. Rams and M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, first public 2014-09-26, arXiv:1409.7485, especially Example 2.1 and Remark 4.4, https://arxiv.org/abs/1409.7485.
3. F. Schur, *Ueber eine besondre Classe von Flächen vierter Ordnung*, Math. Ann. 20 (1882), 254–296 (classical historical reference; no precise first-public calendar day asserted).
