# Maximal Jordan blocks in rooted-tree incidence radicals: exact counts and a finite-field branching transition

## Finding

For any finite rooted tree \(T\), ordered by ancestry, let \(J\) be the Jacobson radical of the incidence algebra \(I(T,\mathbb F_q)\) over a finite field. The nilpotent incidence matrix of a uniformly selected \(N\in J\) has an exact maximal-block law: its largest *possible* Jordan block has size \(h+1\), where \(h\) is the maximum root-to-vertex edge distance, and there is **at most one** such block. A block of size \(h+1\) occurs exactly when at least one root-to-depth-\(h\) path has nonzero coefficients on all its Hasse edges. Arbitrary strict-comparability coefficients away from Hasse edges do not influence this event.

Define a bottom-up probability \(s(v)\) for each tree vertex: a vertex at depth \(h\) has \(s(v)=1\); a leaf at smaller depth has \(s(v)=0\); and every other vertex satisfies
\[
s(v)=1-\prod_{w\text{ child of }v}\left(1-\frac{q-1}{q}s(w)\right).
\]
Then the exact fraction of radical elements whose natural incidence representation has a size-\(h+1\) Jordan block is \(s(\mathrm{root})\). The computation uses \(O(|T|)\) field-independent rational arithmetic operations.

For the full rooted \(b\)-ary tree of height \(h\), where \(b\ge1\), put \(t=(q-1)/q\), \(s_0=1\), and
\[
s_{j+1}=1-(1-ts_j)^b \quad (0\le j<h).
\]
The radical has dimension \(M_h=\sum_{d=1}^h d b^d\). Exactly \(q^{M_h}s_h\) of its \(q^{M_h}\) elements have a size-\(h+1\) block. In particular this is an integer, with the following integer recurrence for an explicit count: writing \(E_h=\sum_{d=1}^h b^d\), \(E_0=0\), \(C_0=1\),
\[
C_{j+1}=q^{b(E_j+1)}-\left(q^{E_j+1}-(q-1)C_j\right)^b,
\qquad q^{M_h}s_h=q^{M_h-E_h}C_h.
\]

For fixed \(b,q\), the limiting probability has a sharp threshold. If \(b=1\), then \(s_h=t^h\to0\). If \(b\ge2\) and \(bt>1\), it decreases to the unique positive solution \(\theta\in(0,1)\) of \(\theta=1-(1-t\theta)^b\), and its error tends to zero exponentially. The only critical pair with integer \(b\ge2\), finite field \(q\ge2\), and \(bt=1\) is \((b,q)=(2,2)\). In that case
\[
s_{h+1}=s_h-\tfrac14s_h^2,\qquad s_h\sim\frac4h.
\]
For binary branching and \(q\ge3\), \(\theta=q(q-2)/(q-1)^2\). Thus the asymptotic positive-density behavior begins at \(q=3\), whereas the binary-field case has inverse-height decay.

## Assumptions and scope

All trees are finite, with a distinguished root, edges directed away from the root, and \(h\ge1\). The partial order is ancestry; \(u<v\) means that \(u\) is a strict ancestor of \(v\). The incidence algebra has basis \(e_{uv}\) for \(u\le v\) and multiplication \(e_{uv}e_{xy}=\mathbf1_{v=x}e_{uy}\). Its radical \(J\) consists of those incidence matrices \(N\) whose diagonal coordinates vanish. Every coordinate \(N(u,v)\) for a strict ancestor pair \(u<v\) is independently uniform in \(\mathbb F_q\) when \(N\) is chosen uniformly in \(J\).

Jordan blocks refer to the \(|V(T)|\times |V(T)|\) matrix of \(N\) in the natural incidence representation on \(\mathbb F_q^{V(T)}\); they do not refer to the much larger operator of left multiplication on the vector space \(J\) or on the full incidence algebra. Every nilpotent matrix is similar over \(\mathbb F_q\) to a sum of zero-eigenvalue Jordan blocks.

## Proof

**1. Maximal-power support.** The \((u,v)\)-entry of \(N^k\) is a sum over strictly increasing chains \(u=u_0<u_1<\cdots<u_k=v\) of the products \(\prod_{i=1}^kN(u_{i-1},u_i)\). Since a strict chain in a height-\(h\) rooted tree has at most \(h\) steps, \(N^{h+1}=0\). A chain of exactly \(h\) steps must begin at the root and end at a depth-\(h\) vertex; each step must be a cover edge. Each such endpoint has a unique root path, so its \(N^h\)-entry is exactly the product of that path's cover coefficients, with no cancellation possible. All other entries of \(N^h\) vanish. Therefore \(\operatorname{rank}(N^h)\in\{0,1\}\). For a nilpotent matrix annihilated by its \((h+1)\)th power, \(\operatorname{rank}(N^h)\) is precisely the number of Jordan blocks of size \(h+1\). This proves both the at-most-one statement and the event criterion.

**2. Independent subtree recursion.** A cover coefficient is nonzero with probability \(t=(q-1)/q\); coefficients on distinct Hasse edges are independent. Starting from vertex \(v\), success means that some descending path reaches absolute depth \(h\) using only nonzero cover coefficients. The child-branch success events are independent. A branch through child \(w\) succeeds with probability \(t s(w)\), hence all children fail with probability \(\prod_w(1-ts(w))\). Terminal conditions at depth \(h\) and shallower leaves give the stated recurrence. Non-Hasse coordinates do not enter the maximal power and are unconstrained. The number of strict ancestor pairs is \(\sum_v\operatorname{depth}(v)\); on a full \(b\)-ary tree it equals \(M_h\). Multiplication by \(q^{M_h}\) gives the exact count.

**3. Integer recurrence.** A rooted \(b\)-ary subtree of height \(j\) has \(E_j\) cover edges, and \(C_j\) successful labelings. For each child branch, there are \(q^{E_j+1}\) labelings of its connecting edge and subtree, of which \((q-1)C_j\) succeed. There are \(b\) independent branches, so the number of labelings with at least one successful branch is \(q^{b(E_j+1)}-(q^{E_j+1}-(q-1)C_j)^b\). Since the whole tree has \(E_{j+1}=b(E_j+1)\) edges, this gives the displayed recurrence and \(C_j=q^{E_j}s_j\).

**4. Threshold and critical law.** Put \(f(x)=1-(1-tx)^b\). The polynomial is increasing and concave on \([0,1]\), with \(f(0)=0\), \(f'(0)=bt\), and \(f(1)<1\). If \(b=1\), iteration gives \(s_h=t^h\). When \(b\ge2\), \(bt>1\) implies strict concavity and a unique positive fixed point \(\theta\), with \(0<f'(\theta)<1\). Iteration starting at \(1\) decreases to \(\theta\), and the mean-value theorem yields eventual geometric contraction. The sole integer equality \(bt=1\) for \(b,q\ge2\) is \(b=q=2\). There \(s_{h+1}=s_h-s_h^2/4\), so \(s_h\downarrow0\) and
\[
\frac{1}{s_{h+1}}-\frac{1}{s_h}
=\frac{1}{4(1-s_h/4)}\longrightarrow\frac14.
\]
Cesàro averaging gives \(1/s_h\sim h/4\), hence \(s_h\sim4/h\). Solving the fixed-point equation for \(b=2\) yields \(\theta=(2t-1)/t^2=q(q-2)/(q-1)^2\) when \(q\ge3\).

## Verification

A self-contained standard-library checker, `checker.py`, builds incidence matrices directly and computes their powers, rather than using the probabilistic recurrence to decide success. It exhaustively enumerates all radical elements in five small full-tree configurations: \((b,h,q)=(1,3,2),(2,1,2),(2,2,2),(2,1,3),(2,2,3)\). Their successful/total counts are respectively \(8/64\), \(3/4\), \(624/1024\), \(8/9\), \(49248/59049\). It also tests a nonbalanced tree, samples additional trees, performs independent matrix multiplication in \(\mathbb F_4\), and numerically checks the critical asymptotic. Run `python3 checker.py`; expected terminal marker is `ALL_TREE_INCIDENCE_TOP_JORDAN_CHECKS_PASSED`.

## Relationship to prior work

Gargate and Gargate (2019, arXiv:1907.06805) count involutions in incidence algebras over finite fields, including special posets, and provide algorithms for more general posets; the present result concerns a different statistic, maximal Jordan-block occurrence for nilpotent incidence-radical matrices. Fuchs and Kirillov (2022, arXiv:2204.00066) investigate Jordan-type distributions of full triangular matrices, whereas the tree ancestry support here permits a unique-path power identity. Van Peski (2024, arXiv:2407.19578) studies ranks of random triangular matrices, not the exact maximal-power distribution of tree incidence radicals.

The survival recurrence and its fixed-point transition are classical Bernoulli branching/percolation mathematics; no novelty is claimed for those probabilistic facts in isolation. The claimed synthesis is the precise incidence-algebra maximal-Jordan-block identification, full-radical integer census, and field-dependent threshold. Priority relative to older or differently phrased incidence-algebra literature has not been independently established.

## Limitations

Only the existence and multiplicity of the *largest possible* block are determined; this is not a census of every Jordan partition. The critical inverse-height asymptotic concerns fixed branching number two and fixed field order two, as the tree height increases, not a limit for a fixed finite algebra. The result depends crucially on rooted-tree unique saturated paths. In posets with multiple maximal chains between comparable vertices, different products can cancel, so the recurrence need not hold. No claim is made about Jordan blocks of left-multiplication operators on the algebra. The paper's novelty comparison does not constitute an exhaustive historical priority certificate.

## References

1. Ivan Gargate and Michael Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805 (first posted 2019-07-16), https://arxiv.org/abs/1907.06805.
2. Dmitry Fuchs and Alexandre Kirillov, *Jordan Types of Triangular Matrices over a Finite Field*, arXiv:2204.00066 (first posted 2022-03-31), https://arxiv.org/abs/2204.00066.
3. Roger Van Peski, *The Rank of a Random Triangular Matrix over \(\mathbb F_q\)*, arXiv:2407.19578 (first posted 2024-07-28), https://arxiv.org/abs/2407.19578.
