# Exact two-leader coherence transition on weighted double stars

## Finding
Let \(D_{p,q}(t)\) be a weighted double-star tree, where \(p,q\ge2\) are integers and \(t>0\). Its adjacent hub vertices are \(u,v\); \(u\) has \(p\) private leaves (class \(A\)) and \(v\) has \(q\) private leaves (class \(B\)). Each leaf edge has resistance \(1\), and the hub-to-hub edge has resistance \(t\) (conductance \(1/t\)). For each two-element, noise-free leader set \(S\), let \(F=V\setminus S\) and define the unnormalized coherence objective \(\mathcal C(S)=\operatorname{tr}((L_{FF})^{-1})\), where \(L\) is the weighted combinatorial Laplacian.

Put \(N=p+q\), \(m=\min\{p,q\}\), and \(t_c=1/(m-1)\). Then
\[
\boxed{\min_{|S|=2}\mathcal C(S)=N+\min\left\{0,\frac{t(m-1)-1}{t+1}\right\}.}
\]
All optimal unordered leader pairs are as follows.

* For \(t>t_c\), the two hubs \(\{u,v\}\) are the unique optimum.
* For \(0<t<t_c\), the optimum consists of the hub with **more** incident leaves and one of the leaves adjacent to the **other**, smaller (or equally large) side. If \(p<q\), these are precisely \(\{v,a\}\) with \(a\in A\); if \(p>q\), precisely \(\{u,b\}\) with \(b\in B\); if \(p=q\), both orientations occur.
* For \(t=t_c\), the optimal pairs are exactly the union of \(\{u,v\}\) and the cross-hub--leaf pairs described for \(0<t<t_c\).

The threshold is sharp. In particular, the optimal pair changes from a hub and a leaf to both hubs as the bridge resistance passes \(1/(\min\{p,q\}-1)\); for unequal leaf multiplicities, the smaller side alone determines the transition.

## Assumptions and scope
All edge conductances are fixed, positive and symmetric. Only leader locations are optimized; exactly two distinct vertices are pinned to the same deterministic signal, all other vertices experience independent unit-intensity white noise, and there is no noise at the leaders. The objective above is twice the usual total stationary variance under the convention \(dX_F=-L_{FF}X_F\,dt+dW_F\). Both conventions have identical minimizers. The graph has \(N+2\) vertices and is connected for every admissible \(t\); \(L_{FF}\) is therefore positive definite for every nonempty pinned set.

## Proof
**Grounded-resistance identity.** When a set of vertices \(S\) is held at voltage zero, injecting unit current at a follower \(x\) yields voltage \((L_{FF}^{-1})_{xx}\); this is the effective resistance from \(x\) to the grounded set. For a weighted tree and two grounded vertices \(s_1,s_2\), let \(P\) be their unique path of total resistance length \(\ell>0\). Let \(y\) be the unique vertex where the path from \(x\) first meets \(P\); write \(h=d_R(x,y)\) and \(z=d_R(s_1,y)\), where \(d_R\) is the sum of edge resistances on a tree path. Parallel reduction of the two grounded path segments gives
\[
(L_{FF}^{-1})_{xx}=h+\frac{z(\ell-z)}{\ell}.
\]
The formula includes path vertices (\(h=0\)) and the zero voltage of pinned vertices; summing over followers proves \(\mathcal C(S)=\sum_{x\notin S}(L_{FF}^{-1})_{xx}\) in the displayed resistance form.

**Exhaustive pair calculation.** Permuting leaves within \(A\) and within \(B\) leaves resistances unchanged, so every unordered pair belongs to one of the eight orbits in the table. A letter \(a\) denotes any member of \(A\) and \(b\) any member of \(B\); distinct letters with the same subscript class represent distinct leaves. By the preceding formula (or ordinary series--parallel reduction), the exact excess over \(N=p+q\) is:

| Leader-pair orbit \(S\) | \(\mathcal C(S)-N\) |
| --- | --- |
| \(\{u,v\}\) | \(0\) |
| \(\{u,a\}\) | \(t(q+1)-1\) |
| \(\{v,b\}\) | \(t(p+1)-1\) |
| \(\{u,b\}\) | \(\dfrac{t(q-1)-1}{t+1}\) |
| \(\{v,a\}\) | \(\dfrac{t(p-1)-1}{t+1}\) |
| \(\{a,a'\}\) | \(\dfrac{N-4+2t(q+1)}2\) |
| \(\{b,b'\}\) | \(\dfrac{N-4+2t(p+1)}2\) |
| \(\{a,b\}\) | \(\dfrac{N-4+t(N-2)}{t+2}\) |

For example, when \(S=\{u,b\}\), every one of the \(p\) leaves in \(A\) has grounded resistance \(1\). The hub \(v\) has resistance \(t/(t+1)\) to the grounded pair \(\{u,b\}\); each of the other \(q-1\) leaves in \(B\) has resistance \(1+t/(t+1)\). The total is \(p+(q-1)(1+t/(t+1))+t/(t+1)=N+[t(q-1)-1]/(t+1)\). For two grounded leaves in \(A\), their hub has grounded resistance \(1/2\), the other \(p-2\) leaves in \(A\) have resistance \(3/2\), hub \(v\) has resistance \(t+1/2\), and all \(q\) leaves in \(B\) have resistance \(t+3/2\), giving the sixth row. The other rows follow by the same two-segment reduction and symmetry; the values are also checked from exact grounded matrices in the standalone verifier.

**Global comparisons.** As \(N\ge4\) and \(t>0\), both same-side leaf-pair excesses and the opposite-side leaf-pair excess are strictly positive; hence none can minimize against \(S=\{u,v\}\). Each hub paired with its **own** leaf is strictly worse than pairing the same hub with a leaf on the opposite side, since
\[
\mathcal C(\{u,a\})-\mathcal C(\{u,b\})
=\frac{t[1+(q+1)t]}{t+1}>0
\]
and, similarly, \(\mathcal C(\{v,b\})-\mathcal C(\{v,a\})=t[1+(p+1)t]/(t+1)>0\). Thus only the two hubs and the two cross-hub--leaf orbits can be optimal. Their costs are \(N\), \(N+[t(q-1)-1]/(t+1)\), and \(N+[t(p-1)-1]/(t+1)\). Since \(t/(t+1)>0\), the better cross orbit uses \(m=\min\{p,q\}\), with both orbits tied exactly when \(p=q\). This orbit has lower cost than the hub pair exactly when \(t(m-1)<1\), ties when equality holds, and has higher cost when \(t(m-1)>1\). All asserted values, pair lists, and sharp boundaries follow. \(\square\)

## Verification
Run `python verify.py` after installing the packages in `requirements.txt`. The verification uses exact rational matrices and compares \(4{,}700\) two-leader grounded-Laplacian inversions across \(100\) choices of \((p,q,t)\) with the corresponding symbolic orbit formula. It also checks every minimizing pair against the closed form for those cases, plus \(15\) rational instances exactly below, at and above the stated threshold. Successful output is `VERIFY_OK exact_grounded_inverses=4700 parameter_instances=100 boundary_instances=15`. These finite tests supplement, but do not replace, the exhaustive symbolic proof above.

## Relationship to prior work
Patterson and Bamieh introduced leader selection for network coherence using grounded Laplacians and combinatorial optimization [1]. Fitch and Leonard developed joint-centrality characterizations and explicit optimal leader placements for paths and cycles, not this weighted double-star family [2]. Patterson, Yi and Zhang proved a resistance-based coherence formula for noise-free leaders and analyzed special trees; their explicit two-leader tree results concern perfect regular rooted trees, and their specialized multi-leader calculations assume unit edge weights [3]. The grounded-resistance identity is therefore prior methodology, not a novelty claim. The contribution here is the closed-form **weighted bistar** classification for all integer leaf multiplicities and positive bridge resistances, including its sharp side-sensitive threshold and all equality cases. No claim is made that a general matrix-inverse or resistance-distance algorithm itself is new.

## Limitations
The claim does not cover fewer than two leaves on either side, more than two pinned leaders, noise-corrupted leaders, asymmetric leaf-edge weights, directed graphs or a different objective such as convergence rate. The comparison to the literature is not an exhaustive guarantee of priority: a specialized treatment of weighted double stars could contain an equivalent formula. Exact matrix calculations on finitely many parameter values do not prove the general theorem; the proof is the eight-orbit resistance computation and strict inequalities.

## References
[1] S. Patterson and B. Bamieh, *Leader Selection for Optimal Network Coherence*, Proceedings of the 49th IEEE Conference on Decision and Control (2010), DOI: 10.1109/CDC.2010.5718151.

[2] K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted 2014-07-07, https://arxiv.org/abs/1407.1569.

[3] S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, first posted 2017-08-23, https://arxiv.org/abs/1708.06873.
