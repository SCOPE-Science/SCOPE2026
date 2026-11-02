# Countably many isolated operator-root limits for injective lacunary weighted shifts

## Finding
Let \(q\ge 2\) be an integer and \(c>0\). On the complex Hilbert space \(H=\ell^2(\mathbb Z)\), with standard basis \((e_k)_{k\in\mathbb Z}\), define \(Te_k=w_ke_{k+1}\), where
\[
w_k=\begin{cases}\exp(-cq^j),&k=q^j\text{ for an integer }j\ge0,\\1,&\text{otherwise.}\end{cases}
\]
Put \(A_n=|T^n|^{1/n}\), \(\alpha=\exp(-cq/(q-1))\), and \(\beta=\exp(-c/(q-1))\); thus \(0<\alpha<\beta<1\). Write \(P_s\) for the orthogonal projection onto \(\overline{\operatorname{span}}\{e_k:k\le s\}\) for any \(s\in\mathbb Z\).

The **complete** weak-operator and strong-operator cluster sets of \((A_n)_{n\ge1}\) coincide and equal
\[
\boxed{\mathcal C=\{tI:\alpha\le t\le\beta\}\;\cup\;\{\alpha I+(\beta-\alpha)P_s:s\in\mathbb Z\}.}
\]
All the step operators \(\alpha I+(\beta-\alpha)P_s\) are isolated connected components of \(\mathcal C\); its only nonsingleton connected component is the scalar interval. Thus this one cluster set has countably infinitely many connected components. The step operators tend strongly to \(\beta I\) as \(s\to+\infty\) and to \(\alpha I\) as \(s\to-\infty\).

For every unit vector \(x\in H\), the scalar asymptotic numerical range defined by Ji and Yang is exactly
\[
\boxed{W_a(T,x)=W_a(T)=[\alpha,\beta],\qquad w_a(T)=\beta.}
\]
Nevertheless \(T\) is an injective contraction with dense range and
\[
\boxed{\|T\|=w(T)=r(T)=1>\beta.}
\]
Here \(w(T)\) is the ordinary numerical radius and \(r(T)\) the spectral radius. The sequence \((A_n)\) has no operator-norm convergent subsequence.

## Assumptions and scope
The index set is the **bilateral** integer lattice and all spike weights are strictly positive. The weight exponent \(cq^j\), rather than \(cj\), is essential: a single spike contributes a nonvanishing amount to a logarithmic moving average at its own scale. The result includes every fixed integer \(q\ge2\) and every real \(c>0\), with no compactness, invertibility, or lower-bound assumption on \(T\). All limits are along integers \(n\to\infty\); none is claimed to be a limit in operator norm.

## Proof
**Step 1: exact diagonal formula.** For integer \(m\), define
\[
F_q(m)=\sum_{j\ge0:q^j\le m}q^j=\begin{cases}0,&m<1,\\(q^{\lfloor\log_q m\rfloor+1}-1)/(q-1),&m\ge1.\end{cases}
\]
Since \(T^ne_k=(\prod_{h=k}^{k+n-1}w_h)e_{k+n}\), the positive operator \(A_n\) is diagonal and satisfies the **exact** identity
\[
A_ne_k=\exp\!\left(-\frac c n[F_q(n+k-1)-F_q(k-1)]\right)e_k.\tag{1}
\]
In particular \(0\le A_n\le I\). A weakly convergent subsequence of bounded diagonal operators has convergent diagonal entries; bounded coordinatewise convergence is also strong convergence on \(\ell^2(\mathbb Z)\) by dominated convergence. The weak- and strong-operator cluster sets therefore agree.

**Step 2: no other limits.** Take any sequence \(n_j\to\infty\), and write \(q^{m_j}\le n_j<q^{m_j+1}\). Passing to a subsequence, suppose \(u_j=n_j/q^{m_j}\to u\in[1,q]\). A fixed initial offset \(F_q(k-1)\) contributes \(o(1)\) to (1).

If \(1<u<q\), then for each fixed coordinate \(k\) the largest spike inside the ending prefix is eventually \(q^{m_j}\). Formula (1) consequently converges on each coordinate to the same scalar
\[
\exp\left(-\frac{cq}{(q-1)u}\right)\in(\alpha,\beta).
\]
If \(u=1\), put \(d_j=n_j-q^{m_j}\ge0\). Pass to a further subsequence such that either \(d_j=d\) is a fixed nonnegative integer or \(d_j\to\infty\). In the first case the spike at \(q^{m_j}\) belongs to the window from \(k\) to \(k+n_j-1\) precisely when \(k\ge1-d\). Therefore the limit is \(\alpha I+(\beta-\alpha)P_{-d}\). In the second case that spike belongs to every fixed-coordinate window, so the limit is \(\alpha I\).

If \(u=q\), put \(d_j=q^{m_j+1}-n_j\ge1\). Again extract a constant-value or diverging subsequence. A fixed value \(d_j=d\) gives inclusion of the next spike precisely for \(k\ge d+1\), and the limit is \(\alpha I+(\beta-\alpha)P_d\). If \(d_j\to\infty\), the next spike is missed by every fixed-coordinate window, giving \(\beta I\). These cases exhaust all possible subsequential limits and prove the inclusion into the displayed set.

**Step 3: all claimed limits occur.** For every fixed \(s\in\mathbb Z\), choose \(n_j=q^j-s\). For each fixed \(k\), the spike \(q^j\) enters the window exactly when \(k\ge s+1\); the lower spikes have sum \((q^j-1)/(q-1)\). Thus (1) tends to \(\beta\) when \(k\le s\) and to \(\alpha\) when \(k>s\), giving the step limit. For any \(1<u<q\), choose \(n_j=\lfloor uq^j\rfloor\) to obtain the interior scalar \(\exp(-cq/((q-1)u))I\). The endpoints occur by taking \(n_j=q^j+j\) for \(\alpha I\) and \(n_j=q^j-j\) for \(\beta I\). This establishes the reverse inclusion.

**Step 4: topology.** The step \(D_s=\alpha I+(\beta-\alpha)P_s\) has diagonal values \(\beta\) at coordinate \(s\) and \(\alpha\) at coordinate \(s+1\). No scalar operator has these two different values; every other \(D_t\) differs from \(D_s\) at one of these two coordinates by \(\beta-\alpha\). The two-coordinate weak-operator neighborhood of radius less than \((\beta-\alpha)/3\) therefore isolates \(D_s\) in \(\mathcal C\). The scalar segment is path connected, and the isolated points are all other connected components. The strong limits as \(s\to\pm\infty\) follow from coordinatewise convergence of \(P_s\) and boundedness.

**Step 5: numerical ranges and spectral radius.** For each unit vector \(x\), the scalar members of \(\mathcal C\) realize every value in \([\alpha,\beta]\) as \(\langle Ax,x\rangle\). Each step member gives
\[
\langle D_sx,x\rangle=\alpha+(\beta-\alpha)\|P_sx\|^2\in[\alpha,\beta].
\]
Every convergent scalar subsequence has an operator-cluster subsequence because the bounded diagonal operators are sequentially compact for pointwise coordinate convergence. Hence \(W_a(T,x)=[\alpha,\beta]\) for all unit \(x\).

All weights lie in \((0,1]\), so \(T\) is an injective contraction. Every basis vector belongs to its range because \(e_{k+1}=T(w_k^{-1}e_k)\); thus its range is dense. The weights tend to zero along the spikes, so \(T\) is not bounded below. For each \(n\), any interval of \(n\) consecutive negative indices has weights all equal to one, proving \(\|T^n\|=1\) and hence \(r(T)=1\). Unit vectors constant on arbitrarily long blocks of consecutive negative indices have \(|\langle Tx,x\rangle|\to1\), so \(w(T)=1\). Finally \(\|A_n\|=1\), whereas each member of \(\mathcal C\) has norm at most \(\beta<1\). Norm continuity rules out an operator-norm convergent subsequence. This completes the proof.

## Verification
The included standard-library-only script `checker.py` independently enumerates spike sums in finite windows and checks exact rational finite-size correction identities for integer bases \(2\) through \(6\), geometric scales, offsets and coordinate indices. Running `python3 checker.py` prints `FINITE_ASSERTIONS_PASSED 18600`. These are finite consistency checks, not a proof of the infinite-dimensional cluster-set classification; the proof above supplies the limiting and exhaustive-subsequence arguments.

## Relationship to prior work
Ji and Yang introduced \(W_a(T,x)\) and the weak-operator cluster set of \(|T^n|^{1/n}\). Their Proposition 4.1 identifies scalar intervals for weighted shifts bounded below; Example 4.2 describes dyadic blocks of weights \(1\) and \(2\), again bounded below. Their abstract also notes that a disconnected cluster set is possible without the lower-bound hypothesis. The result here is an exact, parameter-uniform classification with **countably many isolated components** for a shift with strictly positive weights, dense range and no zero weights. It is not a restatement of connectedness or its failure alone.

## Limitations
The theorem is limited to the specified lacunary family and does not classify arbitrary weighted shifts. The general disconnection phenomenon predates this computation, and priority for the exact countable-component classification has not been independently determined. The latter part of the most relevant 2026 paper's examples section could not be read during comparison; an unrecognized stronger example there remains an originality risk. No independent mathematical audit is claimed.

## References
- Y. Ji and B. Yang, *Asymptotic Numerical Ranges and Invariant Subspaces of Operators*, arXiv:2608.21553v1 (first publicly submitted 21 August 2026); revised v2, 8 September 2026. Relevant material: abstract, introduction, Proposition 4.1 and Example 4.2.
