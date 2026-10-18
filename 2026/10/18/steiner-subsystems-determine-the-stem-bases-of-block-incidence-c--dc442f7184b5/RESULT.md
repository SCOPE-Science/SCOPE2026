# Steiner subsystems determine the stem bases of block-incidence contexts

## Finding

**Theorem (Steiner incidence stem basis).** Let \((V,\mathcal B)\) be a finite Steiner triple system of order \(v\ge7\). Form the binary context \(K\) whose objects are blocks \(B\in\mathcal B\), whose attributes are the points of \(V\), and whose incidence relation is membership. Call \(W\subsetneq V\) a *proper nontrivial subsystem* if \(|W|\ge7\) and, for every two distinct \(a,b\in W\), the unique block \(B(a,b)\) containing that pair lies inside \(W\). Let \(\mathscr M\) comprise the inclusion-minimal proper nontrivial subsystems.

The complete family of Ganter–Wille pseudo-intents of \(K\) is
\[
\mathscr P(K)=\{\{a,b\}:a,b\in V,\ a\ne b\}\ \cup\ \mathscr M.
\]
Consequently its canonical Duquenne–Guigues (stem) implication basis is exactly
\[
\Sigma(K)=\{\{a,b\}\Rightarrow B(a,b)\setminus\{a,b\}: a\ne b\}
\ \cup\ \{W\Rightarrow V\setminus W:W\in\mathscr M\},
\]
where the pair rules are indexed by unordered pairs, and the total number of implications is \(\binom v2+|\mathscr M|\).

**Projective-family corollary.** Set \(V=\mathbb F_2^d\setminus\{0\}\) and let its blocks be \(\{a,b,a+b\}\) for distinct \(a,b\in V\), with \(d\ge4\). The elements of \(\mathscr M\) are precisely the seven-point sets \(U\setminus\{0\}\) where \(U\) ranges over the three-dimensional linear subspaces of \(\mathbb F_2^d\). Thus
\[
|\Sigma(K)|=\binom{2^d-1}{2}+\begin{bmatrix}d\\3\end{bmatrix}_2
=\binom{2^d-1}{2}+\frac{(2^d-1)(2^d-2)(2^d-4)}{168}.
\]
At \(d=4\) there are 105 pair rules and 15 Fano-plane rules, hence 120 canonical implications; at \(d=5\) there are 465 pair rules and 155 Fano-plane rules, hence 620. Writing \(v=2^d-1\), the rule count is asymptotic to \(v^3/168\), although the number of object blocks is only \(v(v-1)/6\).

## Assumptions and scope

A Steiner triple system has a unique three-point block through each pair of distinct points. The construction assumes \(v\ge7\); no claim is made for the degenerate one-block system of order three. All implications follow the usual zero-support-permitted FCA semantics, and the *canonical basis* here means the one-rule-per-pseudo-intent Duquenne–Guigues stem basis, not the size of an arbitrary alternative presentation. All groups, vector spaces, and contexts in the result are finite; the projective corollary ranges over all integers \(d\ge4\). A subsystem in this theorem means a *pair-completion-closed* point set, not any subset of blocks. For \(d=3\) the Fano plane itself is not a proper subsystem and only pair rules remain.

## Proof

**1. The exact closure operator.** For \(S\subseteq V\), its Galois closure \(c(S)=S''\) is the intersection of all blocks that contain \(S\); as usual, an empty family of containing blocks has intersection \(V\). Every point belongs to at least three distinct blocks, and every pair lies in a unique block. Therefore \(c(\varnothing)=\varnothing\), \(c(\{a\})=\{a\}\), and \(c(\{a,b\})=B(a,b)\) for distinct points. If \(|S|=3\), then \(c(S)=S\) precisely when \(S\) is a block, and otherwise \(c(S)=V\). If \(4\le|S|<v\), no block contains \(S\), so \(c(S)=V\); also \(c(V)=V\). Thus the closed sets are exactly the empty set, singletons, blocks, and the full point set.

**2. Pseudo-intents of size two.** In the recursive characterization, a pseudo-intent \(P\) is a nonclosed set such that \(c(Q)\subseteq P\) for every strictly smaller pseudo-intent \(Q\subsetneq P\). Since empty and singleton sets are closed, every two-point set is a pseudo-intent. Its resulting stem implication has exactly the third point of the unique block as consequent.

**3. Higher pseudo-intents force subsystems.** If \(|P|\ge3\) and \(P\) is a pseudo-intent, then every two-element \(Q\subset P\) is a smaller pseudo-intent; hence \(B(a,b)=c(Q)\subseteq P\) for every pair \(a,b\in P\). Therefore \(P\) is pair-completion-closed. A pair-completion-closed three-point set must be a block, and hence is closed rather than a pseudo-intent. If a pair-completion-closed set has at least four points, it inherits a Steiner triple system on its points and so must have size \(\ge7\) (the standard pair count gives \(w(w-1)\) divisible by six, excluding \(w=4,5,6\)). Its closure equals \(V\) when proper.

**4. Exactly the minimal proper subsystems.** Let \(W\) be an inclusion-minimal proper nontrivial subsystem. Its closure is \(V\), and every proper pseudo-intent contained in \(W\) must be a pair: by step 3, any larger one would itself be a proper nontrivial subsystem strictly inside \(W\). The closure of each such pair lies in \(W\) by subsystem closure. Therefore \(W\) satisfies the recursive pseudo-intent condition.

Conversely, let \(P\) be a pseudo-intent with at least three elements. Step 3 makes it a proper nontrivial subsystem. If it strictly contained another proper nontrivial subsystem \(W\), choose an inclusion-minimal nontrivial subsystem \(Q\subseteq W\). By the preceding paragraph, \(Q\) is itself a pseudo-intent. Since \(c(Q)=V\not\subseteq P\), this contradicts the defining condition for \(P\). Hence \(P\) is inclusion-minimal. The generic stem-basis theorem for pseudo-intents then yields exactly the displayed implications, and no others.

**5. Binary projective geometry.** For the specified binary system, pair completion adds \(a+b\). A nonempty point set \(W\) is pair-completion-closed if and only if \(W\cup\{0\}\) is a vector subspace: closure under two distinct nonzero vectors gives their sum, while the sum of an element with itself is zero and zero is already present. A subspace of dimension one supplies a singleton, dimension two supplies a block, and dimension \(\ge3\) supplies a nontrivial subsystem. For \(d\ge4\), inclusion-minimal proper nontrivial subsystems are exactly dimension-three subspaces. Counting ordered independent triples by \((2^d-1)(2^d-2)(2^d-4)\), and dividing by the corresponding number \((2^3-1)(2^3-2)(2^3-4)=168\) of ordered bases of one three-dimensional space, gives the stated Gaussian-binomial formula. The additional term is \(\sim2^{3d}/168\), while the pair count and the number of blocks are both \(\Theta(2^{2d})\). This proves cubic stem-basis growth relative to the number of points.

## Verification

Run the standalone standard-library program `verify.py` with Python 3. It independently computes the Galois closure as the intersection of incident blocks, enumerates pseudo-intents by the recursive definition, and confirms that forward chaining with their implications reproduces the Galois closure on every subset. The exhaustive cases are the seven-point Fano plane, the nine-point affine Steiner triple system, and the fifteen-point binary projective Steiner system. They have respectively 21, 36, and 120 pseudo-intents; the last has 15 additional seven-point pseudo-intents. The program also verifies the Gaussian count for the projective dimensions four, five, and six. These finite tests are not a substitute for the proof for arbitrary systems or dimensions.

## Relationship to prior work

Dubois, Medina, and Prade's 2024 online paper provides and proves equivalence of the general recursive pseudo-intent characterization with the classical Duquenne–Guigues base. In particular, its Definition 20 and Theorem 4 justify the generic basis construction used here; its examined examples are ordinary small formal contexts, not Steiner block-point incidence contexts. Heinlein and Östergård (2022) formalize closure of point-generated Steiner configurations and emphasize the importance of proper subsystems, but their inspected algorithms count design configurations rather than pseudo-intents of the block-incidence context. Horsley and Webb (2020) study Steiner systems avoiding prescribed subsystems, providing independent design-theoretic motivation. Kuznetsov (2004) investigates general canonical-base sizes and demonstrates exponentially large bases for specially constructed contexts; those results do not yield the exact projective-family count. The usual binary-projective subspace enumeration is classical and is not separately claimed as original. The assessed contribution is the structural identification of the canonical premises as minimal proper Steiner subsystems plus pair premises, and the consequent explicit cubic-growth family.

## Limitations

No claim is made that this is the first possible formulation in design-theoretic, closure-system, or logic literature; synonyms such as canonical Horn bases, pseudo-closed sets, line-generation systems, and minimal subdesigns can conceal earlier coverage. No theorem here bounds the *smallest possible noncanonical basis* by the displayed stem-basis count. The 2024 foundations article establishes general pseudo-intent machinery; this result is its specialization with an exact design-theoretic classification, not a replacement for the general theory. The verifier exhausts finite universes only through 15 points, with larger projective orders covered by proof. Independent evaluation has not been performed.

## References

1. D. Dubois, J. Medina, H. Prade, *Extracting attribute implications from a formal context: Unifying the basic approaches*, Information Sciences 689 (2025), 121419; available online 2 September 2024. DOI: 10.1016/j.ins.2024.121419. Open full text: https://rodin.uca.es/handle/10498/36143.
2. D. Heinlein, P. R. J. Östergård, *Algorithms and complexity for counting configurations in Steiner triple systems*, Journal of Combinatorial Designs 30 (2022), 527–546. DOI: 10.1002/jcd.21839. Open full text: https://onlinelibrary.wiley.com/doi/full/10.1002/jcd.21839.
3. D. Horsley, B. S. Webb, *Countable homogeneous Steiner triple systems avoiding specified subsystems*, arXiv:2006.04605, 2020. https://arxiv.org/abs/2006.04605.
4. S. O. Kuznetsov, *On the Intractability of Computing the Duquenne–Guigues Base*, Journal of Universal Computer Science 10 (2004), 927–933.
