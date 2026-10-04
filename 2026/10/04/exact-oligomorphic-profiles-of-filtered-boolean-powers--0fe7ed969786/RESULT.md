# Exact oligomorphic profiles of filtered Boolean powers
## Finding
Let \(\mathbf A\) be a finite simple non-abelian Mal'cev algebra, let \(G=\operatorname{Aut}(\mathbf A)\), and let \(\mathbf B\) be the countable atomless Boolean algebra with Stone space \(X\cong 2^\omega\). Choose pairwise distinct points \(x_1,\dots,x_r\in X\) and idempotents \(e_1,\dots,e_r\in A\) lying in distinct \(G\)-orbits, and put
\[
D=(A^B)^{x_1,\dots,x_r}_{e_1,\dots,e_r}.
\]
For \(k\ge1\), let
\[
q_k=|A^k/G|
\]
be the number of orbits of the diagonal action of \(G\) on \(A^k\). Then the number \(b_k(D)\) of \(\operatorname{Aut}(D)\)-orbits on all ordered \(k\)-tuples is
\[
\boxed{b_k(D)=2^{q_k-r}}.
\]
By Burnside's lemma,
\[
q_k=\frac1{|G|}\sum_{\alpha\in G}|\operatorname{Fix}_A(\alpha)|^k,
\]
so the complete all-tuple orbit profile is explicit from the finite permutation action \(G\curvearrowright A\) and the number \(r\) of distinct filtering-idempotent orbits.

If \(a_k(D)\) denotes the number of orbits on injective ordered \(k\)-tuples, then
\[
\boxed{a_k(D)=\sum_{j=1}^k s(k,j)\,2^{q_j-r}},
\]
where \(s(k,j)\) are the signed Stirling numbers of the first kind. For the unfiltered Boolean power \(r=0\), the corresponding formula is \(b_k=2^{q_k}-1\), since the pointwise orbit-support must be nonempty.

## Assumptions and scope
The formula is stated in the normal form where the filtering idempotents lie in distinct \(\operatorname{Aut}(\mathbf A)\)-orbits. Mayr and Ruškuc prove that every filtered Boolean power by the countable atomless Boolean algebra is isomorphic to one in this form, by deleting repeated filtering orbits. Their Theorem 3.6 gives the required semidirect description of \(\operatorname{Aut}(D)\), and their Theorem 3.9 establishes \(\omega\)-categoricity.

The formula counts automorphism orbits of tuples in the countable structure \(D\). It does not count isomorphism types of finite subalgebras, and it does not assert that two different finite algebras \(\mathbf A\) with the same orbit numbers \(q_k\) have isomorphic filtered Boolean powers.

## Proof
For a tuple \(\bar f=(f_1,\dots,f_k)\in D^k\), define its pointwise orbit map
\[
\tau_{\bar f}:X\longrightarrow A^k/G,
\qquad
\tau_{\bar f}(x)=G\cdot(f_1(x),\dots,f_k(x)),
\]
and its orbit-support
\[
S(\bar f)=\operatorname{im}(\tau_{\bar f}).
\]
Because each \(f_i:X\to A\) is continuous with finite discrete codomain, every fibre of \(\tau_{\bar f}\) is clopen. At a filtering point \(x_i\), every coordinate equals \(e_i\), so
\[
\omega_i:=G\cdot(e_i,\dots,e_i)\in S(\bar f).
\]
The \(\omega_i\) are distinct because the \(e_i\) lie in distinct \(G\)-orbits. Thus every support contains the fixed \(r\)-element set
\[
R_k=\{\omega_1,\dots,\omega_r\}.
\]

Mayr and Ruškuc's Theorem 3.6 says that an automorphism of \(D\) is obtained from a homeomorphism of \(X\) fixing \(x_1,\dots,x_r\), together with a continuous local \(G\)-valued gauge on the punctured Stone space satisfying the stated stabilizer condition near the filtering points. A homeomorphism merely reparametrizes \(\tau_{\bar f}\), while a local gauge acts pointwise within a diagonal \(G\)-orbit. Hence \(S(\bar f)\) is an automorphism invariant.

Conversely, suppose \(S(\bar f)=S(\bar g)\). For each \(\omega\) in this common support, the fibres \(\tau_{\bar f}^{-1}(\omega)\) and \(\tau_{\bar g}^{-1}(\omega)\) are nonempty clopen Cantor subspaces. For a required orbit \(\omega_i\), each corresponding fibre contains the same unique marked filtering point \(x_i\); for nonrequired orbits it contains no marked filtering point. Around each \(x_i\), refine once more to clopen neighborhoods on which both tuples are exactly \((e_i,\dots,e_i)\). Piecewise homeomorphisms of these clopen Cantor pieces therefore glue to a homeomorphism \(h\in(\operatorname{Homeo}X)_{\{x_1,\dots,x_r\}}\) that matches the orbit fibres and is compatible with those exact-value neighborhoods.

After this reparametrization, the two pointwise \(A^k\)-values lie in the same diagonal \(G\)-orbit at every point. Refine \(X\) by the finitely many clopen sets on which the two exact \(A^k\)-values are fixed. On each piece choose one \(\alpha\in G\) carrying the first value to the second, choosing \(\alpha=1\) on neighborhoods of all \(x_i\). This produces a continuous local gauge satisfying Theorem 3.6(2), hence a kernel automorphism carrying the reparametrized \(\bar f\) to \(\bar g\). Therefore
\[
\bar f\text{ and }\bar g\text{ are in the same }\operatorname{Aut}(D)\text{-orbit}
\Longleftrightarrow
S(\bar f)=S(\bar g).
\]

Every subset \(S\subseteq A^k/G\) containing \(R_k\) occurs. Indeed, partition Cantor space into \(|S|\) nonempty clopen pieces, assigning one piece containing \(x_i\) to each required orbit and pieces avoiding all filtering points to the remaining orbits. On each piece make the tuple constant at a chosen representative of its orbit, using \((e_i,\dots,e_i)\) on the piece containing \(x_i\). Thus the orbit set is exactly the family of supersets of \(R_k\), giving
\[
b_k(D)=2^{q_k-r}.
\]
For \(r=0\), exactly the nonempty subsets occur, giving \(2^{q_k}-1\).

Finally, every ordered \(k\)-tuple has an equality partition of its coordinates. If \(a_j\) counts injective \(j\)-tuple orbits, then
\[
b_k=\sum_{j=1}^k {k\brace j}a_j.
\]
Stirling inversion gives the displayed formula for \(a_k\).

There is also a direct growth consequence. If
\[
\lambda=\max_{1\ne\alpha\in G}|\operatorname{Fix}_A(\alpha)|<|A|,
\]
then Burnside's lemma gives
\[
q_k=\frac{|A|^k}{|G|}+O(\lambda^k),
\qquad
\log_2 b_k=\frac{|A|^k}{|G|}+O(\lambda^k).
\]
Hence the orbit profile recovers \(|A|\) from
\[
(\log_2 b_k)^{1/k}\longrightarrow |A|,
\]
and, once \(|A|\) is known, recovers \(|G|\) from \(|A|^k/\log_2 b_k\to |G|\).

## Verification
The accompanying `verify.py` independently computes diagonal finite-group orbits both by direct orbit enumeration and by Burnside's lemma, checks the Stirling transform between all-tuple and injective-tuple profiles, and reproduces the numerical specialization from Mayr and Ruškuc's Example 1.2.

For
\[
\mathbf A=(\mathbb Z_2,x-y+z,\cdot),
\]
Mayr and Ruškuc note that \(\operatorname{Aut}(\mathbf A)\) is trivial and that the two idempotents \(0,1\) supply two filtering orbits. Thus \(q_k=2^k\), \(r=2\), and
\[
b_k=2^{2^k-2}.
\]
For \(k=1,\dots,6\), the checker obtains
\[
1,\ 4,\ 64,\ 16384,\ 1073741824,\ 4611686018427387904.
\]
The corresponding injective profile is
\[
1,\ 3,\ 54,\ 16038,\ 1073580048,\ 4611686002322639760.
\]
It also tests a nontrivial finite permutation action, comparing direct and Burnside orbit counts. Running the script prints `VERIFY_OK`.

## Relationship to prior work
Mayr and Ruškuc define these filtered Boolean powers, prove the semidirect decomposition of their automorphism groups in Theorem 3.6, reduce repeated filtering-idempotent orbits in Corollary 3.8, and cite the Macintyre–Rosenstein characterization to obtain \(\omega\)-categoricity in Theorem 3.9. These results supply the structural ingredients for the support classification above, but the paper does not state the exact tuple-orbit profile \(2^{q_k-r}\).

Macintyre and Rosenstein's 1976 work and Apps's later work establish qualitative \(\aleph_0\)-categoricity results for Boolean structures and Boolean powers. Apps also studies automorphisms of Boolean powers of finite groups. Targeted searches did not locate the exact support-set classification or the closed profile above in those sources.

A published-finding corpus record on the random distributive lattice gives the same numerical expression \(2^{2^k-2}\) for a different structure. That numerical coincidence covers the specialization of Example 1.2 only at the level of a sequence; it does not imply the general theorem \(b_k=2^{q_k-r}\), whose parameter \(q_k\) is the orbit count of an arbitrary finite automorphism action \(\operatorname{Aut}(\mathbf A)\curvearrowright A^k\).

## Limitations
The exact proof uses the countable atomless Boolean algebra, whose Stone space is Cantor space, and the normal form with distinct filtering-idempotent \(G\)-orbits. Other Boolean algebras can have additional topological invariants of clopen fibres, so the support set alone need not classify tuple orbits there.

The literature search was broad but not exhaustive at full-text level for all older Boolean-power papers. In particular, the full 1976 Macintyre–Rosenstein paper and every older group-theoretic Boolean-power source were not all inspected line by line. Because the orbit classification is a short deduction from a strong automorphism theorem, some residual folklore risk remains.

## References
1. Peter Mayr and Nik Ruškuc, *Filtered Boolean powers of finite simple non-abelian Mal'cev algebras*, arXiv:2404.17322. First posted 26 April 2024; current manuscript accepted for the Journal of Algebra.
2. Angus Macintyre and Joseph G. Rosenstein, *\(\aleph_0\)-categoricity for rings without nilpotent elements and for Boolean structures*, Journal of Algebra 43 (1976), 129–154. DOI: 10.1016/0021-8693(76)90148-4.
3. A. B. Apps, *Boolean powers of groups*, Mathematical Proceedings of the Cambridge Philosophical Society 91 (1982), 375–396. DOI: 10.1017/S0305004100059442.
4. A. B. Apps, *\(\aleph_0\)-Categorical Finite Extensions of Boolean Powers*, Proceedings of the London Mathematical Society s3-47 (1983), 385–410. DOI: 10.1112/plms/s3-47.3.385.
