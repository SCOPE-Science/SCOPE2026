# Chromatic compression of finite actual-effectivity action representations

## Finding

Let \(A=\{1,\ldots,k\}\), where \(k\ge 2\), and let \(F=(W,(\Sigma_i(w))_{i\in A,w\in W})\) be a finite actual-effectivity neighbourhood frame satisfying the three concurrent-game representability conditions: every family \(\Sigma_i(w)\) is nonempty and consists of nonempty subsets of \(W\); all agents have the same union \(O_w=\bigcup\Sigma_i(w)\); and every tuple \(S_i\in\Sigma_i(w)\) has nonempty intersection \(\bigcap_i S_i\).

For each world \(w\), form the **joint-outcome conflict graph** \(G_w\) with vertex set \(O_w\). Its distinct vertices \(u,v\) are adjacent exactly when there are \(S_i\in\Sigma_i(w)\) for all agents such that \(\{u,v\}\subseteq\bigcap_i S_i\). Put \(d_w=\chi(G_w)\).

**Theorem (instance-sensitive chromatic compression).** For any positive integers \(b_i(w)\) such that
\[
\prod_{j\ne i} b_j(w)\ \ge\ d_w\qquad\text{for every agent }i,
\]
there is a deterministic concurrent-game structure on \(W\), realizing precisely the given actual-effectivity families, with **exactly \(b_i(w)\) distinguishable actions per neighbourhood** \(S\in\Sigma_i(w)\) for agent \(i\) at \(w\). No other action types are needed. In particular, a uniform factor \(b(w)=\lceil d_w^{1/(k-1)}\rceil\) suffices at \(w\).

The result is an attained **sufficient** multiplicity bound; neither the chromatic number nor the displayed product inequality is asserted to be necessary for a particular frame. In contrast with earlier universal bounds in terms of \(r_w=|O_w|\), it may compress arbitrarily: for two agents and \(\Sigma_1(w)=\Sigma_2(w)=\{\{0,j\}:1\le j\le n\}\), the outcome set has \(n+1\) elements while the conflict graph is a star and has \(d_w=2\). Thus two actions per neighbourhood suffice for every \(n\ge 1\).

## Assumptions and scope

The carrier and every neighbourhood family are finite, the state set is unchanged, each action determines exactly one prescribed neighbourhood through its possible outcomes against all other actions, and transitions are deterministic functions of the complete action profile. There are at least two agents. At worlds with different families the construction is performed separately, with independently chosen copy factors \(b_i(w)\). A proper graph coloring may be found by brute force; no efficient computation of \(\chi(G_w)\) is claimed.

## Proof

Fix a world and suppress its subscript. Each simultaneous neighbourhood intersection \(I=\bigcap_i S_i\) is nonempty and is a clique of \(G\): every distinct \(u,v\in I\) witnesses its edge. Choose a proper coloring \(c:O\to\{0,\ldots,d-1\}\). Consequently, \(c\) is injective on every such intersection \(I\).

Let \(p\) index a largest copy factor \(b_p\). Since the complement product at \(p\) is a minimum among the complement products, \(B=\prod_{j\ne p}b_j\ge d\). Give agent \(i\) the actions \((S_i,t_i)\), where \(S_i\in\Sigma_i\) and \(t_i\in\mathbb Z/b_i\mathbb Z\). Define the mixed-radix signature
\[
H(t_1,\ldots,t_k)=\bigl((t_j-t_p)\bmod b_j\bigr)_{j\ne p}
\]
with codomain \(Q=\prod_{j\ne p}\mathbb Z/b_j\mathbb Z\). Choose a surjection \(\pi:Q\twoheadrightarrow\{0,\ldots,d-1\}\).

**Slice-surjectivity lemma.** For every \(i\), fixing any one copy index \(t_i\) leaves the map \(H\) onto \(Q\). When \(i=p\), a desired signature \(y\) is obtained by choosing \(t_j=y_j+t_p\pmod{b_j}\) for \(j\ne p\). When \(i\ne p\), choose \(t_p\in\{0,\ldots,b_p-1\}\) with \(t_p\equiv t_i-y_i\pmod{b_i}\), possible because \(b_p\ge b_i\). For each remaining \(j\ne i,p\), set \(t_j=y_j+t_p\pmod{b_j}\). This realizes every \(y\in Q\) while \(t_i\) remains fixed. Thus \(\pi\circ H\) is onto the color palette on every one-coordinate slice.

At a complete profile \(((S_1,t_1),\ldots,(S_k,t_k))\), take \(I=\bigcap_i S_i\), and \(a=\pi(H(t_1,\ldots,t_k))\). If \(I\) contains an element of color \(a\), output that element; it is unique since \(I\) is a clique and \(c\) is proper. If \(I\) contains none, output any fixed element of \(I\), such as its first in a prescribed order. Every output belongs to all chosen \(S_i\).

Now fix agent \(i\), a prescribed neighbourhood \(S_i\), and its copy label \(t_i\). Its possible outcomes are contained in \(S_i\). Conversely, take any \(u\in S_i\). Uniform union \(O=\bigcup\Sigma_j\) guarantees that for each other agent \(j\) some \(S_j\in\Sigma_j\) contains \(u\). Hence \(u\in I=\bigcap_j S_j\). By the lemma choose the other labels with \(\pi(H)=c(u)\). Since coloring is injective on \(I\), the outcome rule selects exactly \(u\). Thus the full possible-outcome set of \((S_i,t_i)\) equals \(S_i\). Every prescribed neighbourhood occurs, and no additional one occurs. Apply the construction at each world independently. This proves the theorem.

For the example, \(O=\{0,1,\ldots,n\}\), and the complete intersections are either \(\{0\}\) or \(\{0,j\}\). Hence the only conflict edges are \(\{0,j\}\), so \(G\) is a star, \(d=2\), and the two-agent condition allows \(b_1=b_2=2\). The reachable-range factor grows as \(n+1\), whereas this sufficient copy factor is constant.

## Verification

The bundled standard-library program `verify.py` independently reconstructs the conflict graph, finds a proper coloring, builds the deterministic transition table, and checks **for every action** that its full outcome set over every other action profile equals its prescribed neighbourhood. It enumerates all \(845\) admissible ordered two-agent neighbourhood-family pairs on a three-element outcome set, checks asymmetric three-agent profiles, whole-range boundary cases, star families, and singleton-intersection families. Execute `python verify.py`; the success marker is `CHROMATIC_EFFECTIVITY_COMPRESSION_OK`. These finite tests corroborate but do not prove the theorem for arbitrary finite frames. The slice-surjectivity proof and exact-outcome reconstruction supply the general argument.

## Relationship to prior work

Ciardelli's representation theorem (2026) characterizes representable actual-effectivity frames and gives a state-indexed action realization. A published root-size refinement gives \(\lceil |O_w|^{1/(k-1)}\rceil\) copies per neighbourhood and proves that factor worst-case sharp. The current theorem does not contradict worst-case sharpness: it refines *particular instances* by observing that only outcomes which can occur together in a complete neighbourhood intersection need distinct colors.

An earlier result on chromatic compression of proper relational covers also uses a conflict graph, but there the objects are accessible pairs of epistemic worlds and the goal is a bounded-morphic relational cover. Here the objects are joint **effectivity outcomes**, and the output is a deterministic simultaneous-action transition realizing *exact* individual action outcome sets; the relational-cover theorem supplies no such implication. The full published statements and proofs of both comparisons were inspected.

## Limitations

The theorem gives an achievable action budget, **not** an optimality or minimality characterization for individual frames. Chromatic number can be computationally expensive; no polynomial algorithm or asymptotic gain in all instances is claimed. It does not cover infinite frames or a one-agent instance. Related earlier general representation methods could potentially express the same sufficient construction under different terminology; historical priority is not guaranteed. The finite checker covers only explicitly stated small cases.

## References

1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866v1 (first public 2026-06-30), EPTCS 447 (2026), DOI 10.4204/EPTCS.447.13. https://arxiv.org/html/2606.31866
2. *Sharp root-size action realization for finite actual-effectivity frames*, publicly accessible research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-root-size-action-realization-for-finite-actual-effectivity--114a0e0912e6
3. *Sharp local-range compression for actual-effectivity representations*, publicly accessible research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-local-range-compression-for-actual-effectivity-representat--4bce89f50bf5
4. *Chromatic compression of proper relational covers*, publicly accessible research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-chromatic-compression-of-proper-relational-covers--eb84d71bb78d
