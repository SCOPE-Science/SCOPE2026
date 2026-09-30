# Uniform introreducibility spectra contain a full Turing cone
## Finding
For every infinite introenumerable set \(A\), there is an infinite uniformly introreducible set \(R\subseteq A\) such that \(A\leq_T R\) and
\[
\operatorname{UIdeg}(R)
:=\{\deg_T(B):B\in[R]^\omega\text{ is uniformly introreducible}\}
=
\{\mathbf b:\mathbf b\geq\deg_T(R)\}.
\]
Thus every introenumerable set contains a uniformly introreducible core whose uniformly introreducible-subset degree spectrum is exactly a full upper Turing cone.

There is a stronger uniform form. Fix a decoder \(\Theta\) for \(R\), so that \(\Theta^D=R\) for every infinite \(D\subseteq R\). Then one ordinary Turing functional \(\Lambda\), depending only on this fixed decoder and on the computable coding conventions, works simultaneously for a family \(\{B_X:R\leq_T X\}\): for every such \(X\), \(B_X\subseteq R\), \(B_X\equiv_T X\), and
\[
\Lambda^C=B_X
\qquad\text{for every infinite }C\subseteq B_X.
\]
Consequently the family realizes every degree above \(\deg_T(R)\) while sharing one reconstruction procedure.

## Assumptions and scope
All sets are subsets of \(\omega\), and reducibility is ordinary Turing reducibility. For an infinite set \(Y\), let \(p_Y(n)\) denote its increasing enumeration.

A set \(Y\) is uniformly introreducible when there is one Turing functional \(\Phi\) such that \(\Phi^D=Y\) for every infinite \(D\subseteq Y\).

The ownership input is Cintioli's theorem: every infinite introenumerable \(A\) contains an infinite uniformly introreducible \(R\), and in the stronger formulation there are ordinary functionals \(\Psi,\Theta\) such that every infinite \(D\subseteq R\) satisfies \(\Psi^D=A\) and \(\Theta^D=R\). In particular, taking \(D=R\) gives \(A\leq_T R\).

Fix once and for all a computable bijection \(h:2^{<\omega}\to\omega\). For \(X\subseteq\omega\), define its finite-initial-segment code
\[
S_X=\{h(X\upharpoonright n):n\in\omega\}.
\]
The standard Dekker-code argument gives a single computable decoding scheme, independent of \(X\), that reconstructs \(X\), and hence \(S_X\), from every infinite subset of \(S_X\).

## Proof
Choose \(R\subseteq A\) and a fixed functional \(\Theta\) from Cintioli's theorem, with
\[
\Theta^D=R
\quad\text{for every infinite }D\subseteq R.
\]

First prove the lower bound on the spectrum. If \(B\subseteq R\) is infinite, then \(\Theta^B=R\). Hence
\[
R\leq_T B,
\]
so every degree represented by an infinite subset of \(R\), and therefore every degree in \(\operatorname{UIdeg}(R)\), lies above \(\deg_T(R)\).

For the converse, let \(X\) be any set with \(R\leq_T X\). Define
\[
B_X=\{p_R(n):n\in S_X\}.
\]
Because \(R\leq_T X\), the principal function \(p_R\) is computable from \(X\); because \(S_X\leq_T X\), it follows that
\[
B_X\leq_T X.
\]

Now let \(C\subseteq B_X\) be infinite. Since \(C\subseteq R\), the fixed decoder \(\Theta\) computes \(R\) from \(C\). Using the recovered set \(R\), compute the index set
\[
I_C=\{n:p_R(n)\in C\}.
\]
This is an infinite subset of \(S_X\). The universal finite-initial-segment decoder therefore reconstructs \(X\) from \(I_C\), and from the recovered pair \((R,X)\) it computes \(S_X\) and then \(B_X\). These operations compose into one ordinary functional \(\Lambda\) that depends on the fixed index for \(\Theta\) but not on \(X\). Hence
\[
\Lambda^C=B_X
\quad\text{for every }X\geq_T R\text{ and every infinite }C\subseteq B_X.
\]
Thus each \(B_X\) is uniformly introreducible, with a decoder common to the whole family.

Taking \(C=B_X\) in the same computation shows that \(B_X\) computes \(X\): recover \(R\), recover the exact index set \(I_{B_X}=S_X\), and decode \(X\). Therefore
\[
X\leq_T B_X\leq_T X,
\]
so \(B_X\equiv_T X\).

Every degree \(\mathbf b\geq\deg_T(R)\) has a representative \(X\) with \(R\leq_T X\), and the corresponding \(B_X\) has degree \(\mathbf b\). This proves the reverse inclusion and hence the exact cone equality.

## Verification
The proof was checked at the level of Turing functionals rather than only degrees. The crucial uniformity point is that the decoder for a finite-initial-segment code is independent of the coded real: from any infinite subset of \(S_X\), arbitrarily long compatible initial segments of \(X\) are available, so each bit of \(X\) is eventually determined. After \(R\) is reconstructed by the fixed \(\Theta\), the map between elements of \(R\) and their indices under \(p_R\) is decidable relative to \(R\), making \(I_C\) uniformly computable from \(C\).

The two degree inequalities were checked separately. The forward inequality \(B_X\leq_T X\) uses the hypothesis \(R\leq_T X\). The reverse inequality \(X\leq_T B_X\) uses uniform introreducibility of the ambient core \(R\) to recover \(R\) before decoding the index set. No claim is made for a degree below \(\deg_T(R)\), and the lower-bound argument rules such a degree out for every infinite subset of \(R\), not only for the constructed family.

## Relationship to prior work
Cintioli proves the recent existence theorem that every infinite introenumerable set contains a uniformly introreducible subset, with a common reconstruction procedure for the selected subset and a separate procedure recovering the original set from every infinite subset. The source does not state the cone-spectrum conclusion above.

Kumar and Shelah prove a closely related nonuniform degree-spectrum lemma: if \(A\) is introreducible of degree \(\mathbf d\), then the degrees of introreducible subsets of \(A\) contain the Turing cone above \(\mathbf d\). Their proof also pulls a Dekker code back along the increasing enumeration of \(A\). The additional point here is that when the ambient core has a fixed uniform decoder, the pullback construction can itself be decoded uniformly, and in fact one decoder works for the entire cone family. Combining this observation with Cintioli's theorem applies it to every introenumerable set and makes the spectrum inside the selected core exactly the cone, because all of its infinite subsets already compute that core.

The classical paper of Jockusch introduced uniform introreducibility and established many structural facts about it. Targeted comparisons against available indexed material, later detailed citations, and exact-phrase searches did not locate the common-decoder cone statement. The complete publisher text of that article was not available in the accessible literature path, so a residual priority risk remains for older implicit coverage.

## Limitations
The base degree \(\deg_T(R)\) need not equal \(\deg_T(A)\). Cintioli explicitly does not claim that the selected uniformly introreducible subset can always be chosen Turing-equivalent to the original introenumerable set, so the theorem does not place the cone base exactly at \(\deg_T(A)\).

The result is qualitative in degree structure. It gives no complexity bound on an index for the common decoder as a function of a presentation of \(A\), and it does not assert that the family \(X\mapsto B_X\) is uniformly computable from an arbitrary code for the original introenumerable set.

The originality assessment is best-of-knowledge and carries the stated residual risk from incomplete direct access to the 1968 article; no independent audit has been performed.

## References
Patrizio Cintioli, “Every introenumerable set contains a uniformly introreducible subset,” arXiv:2609.17605v1, first public version 2026-09-13.

Ashutosh Kumar and Saharon Shelah, “Ultrafilters and Turing Independence,” 2026, Lemma 2.2.

Carl G. Jockusch Jr., “Uniformly Introreducible Sets,” Journal of Symbolic Logic 33 (1968), 521–536, DOI 10.2307/2271359.

Noam Greenberg, Matthew Harrison-Trainor, Ludovic Patey, and Daniel Turetsky, “Computing Sets from All Infinite Subsets,” Transactions of the American Mathematical Society 374 (2021), 8131–8160.
