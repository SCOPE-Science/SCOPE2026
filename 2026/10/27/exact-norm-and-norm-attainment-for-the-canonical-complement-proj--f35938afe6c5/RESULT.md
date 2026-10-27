# Exact norm and norm-attainment for the canonical complement projections in the Loy–Willis approximate identity

## Finding

Let \(X=C_0([0,\omega_1))\) be the scalar-valued continuous functions on the ordinal interval with the order topology, equipped with the supremum norm. For a closed unbounded set (club) \(D\subseteq[0,\omega_1)\), put

\[
\pi_D(\alpha)=\min(D\cap[\alpha,\omega_1)),\qquad P_Df=f\circ\pi_D,\qquad Q_D=I-P_D.
\]

Then

\[
\|Q_D\|=2\quad\text{for every }D\subsetneq[0,\omega_1)\text{ that is a club},
\]

the norm is attained by \(f=\mathbf 1_{\{\xi\}}-\mathbf 1_{[\xi+1,\eta]}\) for each gap \([\xi,\eta)\) with \(\xi=0\) or a successor. In the full-club case, \(Q_{[0,\omega_1)}=0\). Thus the bound \(\|Q_D\|\le 2\) for the canonical approximate-identity projections is sharp at every proper club index. This statement concerns this specific family, not all possible bounded approximate identities.

## Assumptions and scope

The interval \([0,\omega_1)\) carries its order topology, and \(C_0([0,\omega_1))\) is normed by \(\|f\|_\infty=\sup_{\alpha<\omega_1}|f(\alpha)|\). A club is a closed and unbounded subset of this ordinal interval. For each club \(D\), the map \(\pi_D\) is the increasing retraction onto \(D\). The primary source proves that \(P_D\) is a projection of norm one and that, when \(D\) is proper, the complement of \(D\) is a union of gaps \([\xi,\eta)\) with \(\xi=0\) or \(\xi\) a successor ordinal, and \(\eta\in D\), \(\xi<\eta\).

## Proof

Because \(\|P_D\|=1\), the triangle inequality gives \(\|Q_D\|=\|I-P_D\|\le 1+\|P_D\|=2\).

Now let \(D\) be a proper club. Choose one gap \([\xi,\eta)\subseteq[0,\omega_1)\setminus D\) from the gap decomposition above. Thus \(\xi<\eta\), \(\eta\in D\), and \(\xi\) is either zero or a successor ordinal. In the ordinal order topology, both \(\{\xi\}\) and \([\xi+1,\eta]\) are clopen. Define

\[
f=\mathbf 1_{\{\xi\}}-\mathbf 1_{[\xi+1,\eta]}.
\]

The supports of these two indicators are disjoint clopen sets, so \(f\) is continuous, has compact support, and satisfies \(\|f\|_\infty=1\). Since there is no point of \(D\) in \([\xi,\eta)\), one has \(\pi_D(\xi)=\eta\). Hence \(f(\xi)=1\), \(f(\eta)=-1\), and

\[
(Q_Df)(\xi)=f(\xi)-f(\pi_D(\xi))=1-(-1)=2.
\]

It follows that \(\|Q_D\|\ge \|Q_Df\|_\infty/\|f\|_\infty\ge2\). Together with the upper bound, this proves \(\|Q_D\|=2\). If \(D=[0,\omega_1)\), then \(\pi_D\) is the identity, so \(P_D=I\) and \(Q_D=0\).

## Verification

The proof uses only the norm-one projection property and the published gap decomposition for a proper club. The lower bound is witnessed by the explicit compactly supported function \(f\) above; it is not inferred from finite numerical experiments. The argument handles every proper club uniformly. No claim is made about the smallest possible bound among all left approximate identities of the Loy–Willis ideal.

## Relationship to prior work

Kania, Koszmider, and Laustsen construct \(Q_D=I-P_D\) as a net of projections in the Loy–Willis ideal and prove \(\|Q_D\|\le2\), which gives a bounded left approximate identity. Their Lemma 2.14(v) supplies the gap decomposition used here, and their proof of Corollary 1.9 supplies the approximate-identity context. The inspected statement gives the upper bound but does not state equality for each proper club. Targeted published-finding corpus searches returned related complement-projection and approximate-identity findings for different spaces or operators, not this ordinal retraction family. The present claim sharpens only the norm of these canonical members; it does not establish that every approximate identity must have bound at least two.

## Limitations

The result is restricted to the canonical projections \(Q_D\) associated with clubs in \([0,\omega_1)\). It does not determine the optimal bound over arbitrary bounded left or two-sided approximate identities, and it makes no assertion about other ordinal intervals or other Banach spaces. Bibliographic search absence is not proof that no differently phrased prior observation exists.

## References

1. T. Kania, P. Koszmider, and N. J. Laustsen, “A weak\(^*\)-topological dichotomy with applications in operator theory,” *Transactions of the London Mathematical Society* 1 (2014), no. 1, 1–28. Earliest public version: arXiv:1303.0020v1, submitted 2013-02-28; DOI: 10.1112/tlms/tlu001. Relevant statements: Lemma 2.14(v), Corollary 1.9, and the proof of Corollary 1.9.
