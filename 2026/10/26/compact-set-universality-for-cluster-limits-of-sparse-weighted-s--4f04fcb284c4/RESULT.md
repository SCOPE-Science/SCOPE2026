# Compact-set universality for cluster limits of sparse weighted-shift modulus roots

## Finding
Let \(K\) be an arbitrary nonempty compact subset of \((0,\infty)\). There is an injective contractive unilateral weighted shift \(T\) on \(\ell^2(\mathbb N)\) for which the weak-operator and strong-operator cluster sets of \(A_n=|T^n|^{1/n}\) coincide and equal
\[
\mathcal C_K
=\{tI:e^{-a_*}\le t\le1\}
\ \cup\ \bigcup_{h=1}^{\infty}\{P_h+e^{-a}(I-P_h):a\in K\},
\qquad a_*=\max K,
\]
where \(P_h\) is the projection onto the first \(h\) coordinate vectors. Each fixed-\(h\) subset is both closed and open in \(\mathcal C_K\) and is homeomorphic to \(K\). Thus, taking \(K\) to be a Cantor set makes the operator cluster set have uncountably many connected components. Nevertheless, every unit vector \(x\) has the same scalar asymptotic numerical range:
\[
\operatorname{Clust}_{n\to\infty}\langle A_nx,x\rangle=[e^{-a_*},1].
\]
Here \(\operatorname{Clust}\) means limits along subsequences whose indices tend to infinity.

## Assumptions and scope
Work over the complex Hilbert space \(H=\ell^2(\mathbb N)\), with canonical basis \((e_k)_{k\ge1}\). Let \(N_j=2^{2^j}\) for \(j\ge1\). Choose \(a_j\in K\) so that the cluster set of the scalar sequence \((a_j)\) is precisely \(K\); for example, repeat successively longer finite nets of \(K\). Let
\[
w_m=\begin{cases}
\exp(-a_jN_j),&m=N_j\text{ for some }j,\\
1,&\text{otherwise},
\end{cases}\qquad Te_k=w_ke_{k+1}.
\]
Every weight is positive, \(\|T\|=1\), and \(T\) is not bounded below. The cluster-set equality concerns all operator subsequential limits of the specified single shift, not arbitrary weighted shifts. The exponent \(1/n\) is taken by the positive functional calculus.

## Proof
**1. Exact diagonal representation.** Since
\[
T^ne_k=\left(\prod_{m=k}^{k+n-1}w_m\right)e_{k+n},
\]
we have
\[
A_ne_k=\exp\!\left(-\frac1n
\sum_{j:\,k\le N_j\le k+n-1}a_jN_j\right)e_k.
\tag{1}
\]
All \(A_n\) are positive diagonal contractions. On such a uniformly bounded family, weak-operator convergence is equivalent to coordinatewise convergence and implies strong-operator convergence: convergence on each basis vector extends to arbitrary vectors by a finite-coordinate approximation, with contraction bounds controlling the tails. In particular, weak and strong cluster points coincide.

**2. Superlacunary error.** Put \(Q_j=\sum_{i\le j}a_iN_i\). From \(0<a_i\le a_*\) and the explicit sequence of sites,
\[
\frac{Q_{j-1}}{N_j}\le a_*\frac{\sum_{i<j}N_i}{N_j}\longrightarrow0,
\qquad \frac{Q_j}{N_j}=a_j+o(1).
\tag{2}
\]
For every fixed coordinate \(k\), finitely many earliest sites below \(k\) contribute at most a constant independent of \(n\), hence disappear after division by \(n\).

**3. No other cluster points.** Choose any subsequence of \(A_n\) converging weakly, and relabel its indices as \(n\to\infty\). Let \(j=j(n)\) be the unique index with \(N_{j-1}\le n<N_j\) (put \(N_0=1\)) and let \(h_n=N_j-n\ge1\). Since \(n\to\infty\), also \(j\to\infty\). Pass to a further subsequence on which either \(h_n=h\) is a fixed positive integer or \(h_n\to\infty\).

In the first case, \(n=N_j-h\). Passing to a further subsequence, compactness of \(K\) gives \(a_j\to a\in K\). For a fixed coordinate \(k\), the site \(N_j\) lies in \([k,k+n-1]\) exactly when \(k\ge h+1\), once \(j\) is large. Equation (2) eliminates earlier sites, and \(N_j/n\to1\). Equation (1) therefore converges to \(1\) for \(k\le h\) and to \(e^{-a}\) for \(k\ge h+1\), yielding \(P_h+e^{-a}(I-P_h)\).

In the second case, the next site \(N_j\) lies outside \([k,k+n-1]\) for every fixed \(k\), eventually. All previous sites except a fixed finite set lie inside that interval. Thus the exponent in (1) differs from \(Q_{j-1}/n\) by \(o(1)\), independently of the fixed coordinate. Since \(n\ge N_{j-1}\),
\[
0\le Q_{j-1}/n\le a_*+o(1).
\]
Every convergent subsubsequence therefore has scalar limit \(e^{-s}I\) with \(0\le s\le a_*\). This establishes the upper inclusion in the displayed formula for \(\mathcal C_K\).

**4. Every listed limit occurs.** Fix \(a\in K\) and \(h\ge1\). Choose indices \(j\to\infty\) with \(a_j\to a\), and set \(n=N_j-h\). The first case in Step 3 proves strong convergence to \(P_h+e^{-a}(I-P_h)\).

For \(0<s<a_*\), choose \(j\to\infty\) with \(a_j\to a_*\) and \(a_j>s\), and put \(n=\lceil a_jN_j/s\rceil\). Then \(N_j\le n<N_{j+1}\) eventually; the \(N_j\) spike is included in every fixed-coordinate window, while the \(N_{j+1}\) spike is not. Equation (2) gives the scalar limit \(e^{-s}I\). To obtain \(s=a_*\), instead take \(n=N_j\) along the same subsequence. Finally, \(n=\lfloor\sqrt{N_jN_{j+1}}\rfloor\) yields \(I\). This completes the reverse inclusion.

**5. Topology and numerical ranges.** For a fixed \(h\ge1\), the continuous coordinate difference
\[
F_h(A)=\langle Ae_h,e_h\rangle-\langle Ae_{h+1},e_{h+1}\rangle
\]
vanishes on the scalar interval and on all step families except the \(h\)-th. On that family it equals \(1-e^{-a}\ge1-e^{-\min K}>0\). Hence the \(h\)-th family is clopen in \(\mathcal C_K\). The map \(a\mapsto P_h+e^{-a}(I-P_h)\) is a homeomorphism from \(K\) onto this family, even in operator norm. The scalar interval is one connected component; all remaining connected components are exactly those within these clopen copies of \(K\). For Cantor \(K\), this supplies uncountably many components.

For every unit \(x\), the scalar limits already realize all numbers in \([e^{-a_*},1]\) as \(\langle Ax,x\rangle\). Every additional step operator is bounded between \(e^{-a_*}I\) and \(I\), so its expectation lies in the same interval. Compactness and the cluster-set description give precisely the displayed scalar asymptotic numerical range.

## Verification
The self-contained `check.py` evaluates (1) against an independent index scan, exercises the limits near sparse sites, tests scalar dilation subsequences and checks the coordinate-jump separation. It passed 4,997 finite tests on the packaged source. These finite computations do not prove completeness of the infinite cluster set; Steps 1–5 provide that proof. No numerical approximation to \(e^{-a_jN_j}\) is required to define the operator.

## Relationship to prior work
Ji and Yang introduced this modulus-root asymptotic numerical range and showed that bounded-below shifts have only scalar operator cluster points. Their Example 4.3 constructs one non-bounded-below shift with a disconnected weak-operator cluster set, detected by two matrix-coefficient accumulation values. The present theorem gives a complete strong- and weak-operator cluster-set classification for a variable-amplitude superlacunary family and realizes an arbitrary compact set as a clopen piece. It also shows that these different operator-topological components can remain invisible to every scalar asymptotic numerical range. The earlier disconnectedness construction is expressly acknowledged and not claimed as new.

## Limitations
The realization theorem concerns one engineered class of positive weighted shifts, not all possible modulus-root cluster sets or all operators. The component classification depends on \(\min K>0\); including zero among spike amplitudes could merge a step family with the scalar interval. The result does not establish any invariant-subspace criterion beyond the earlier paper. A search of inspected and indexed sources did not reveal a covering theorem, but older or unindexed operator-asymptotics literature may contain equivalent formulations. Independent scientific validation has not been performed.

## References
- Y. Ji and B. Yang, *Asymptotic Numerical Ranges and Invariant Subspaces of Operators*, arXiv:2608.21553v1 (first public August 21, 2026), especially Theorems 2.4 and 2.10, Proposition 4.1, and Example 4.3. https://arxiv.org/abs/2608.21553
- The classical diagonal form of powers of unilateral weighted shifts, recalled and proved directly in Step 1; no external classification theorem is required.
