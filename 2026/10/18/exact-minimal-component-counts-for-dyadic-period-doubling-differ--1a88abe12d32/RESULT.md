# Exact minimal-component counts for dyadic period-doubling difference lifts

## Finding
Let \(\vartheta\) be the binary substitution \(\vartheta(1)=10\), \(\vartheta(0)=11\), and let \(Y\subset\{0,1\}^{\mathbb Z}\) be its two-sided substitution subshift. For every integer \(r\ge 2\), set \(D=2^r\) and define the permutative difference block code
\[
\eta_D(x)_j=x_{j+D}+x_j\pmod 2,\qquad x\in\{0,1\}^{\mathbb Z},\quad j\in\mathbb Z.
\]
Put \(X_D=\eta_D^{-1}(Y)\), with the bilateral shift acting on both spaces.

**Theorem.** The shift on \(X_D\) has exactly \(2^{D-1}=2^{2^r-1}\) pairwise disjoint minimal components, whose union is the full lift. Each minimal component contains **exactly two** points of \(\eta_D^{-1}(y)\) for every \(y\in Y\). In particular the five-symbol difference lift (\(r=2\), \(D=4\)) has exactly eight minimal components of uniform fibre rank two, and the nine-symbol lift (\(r=3\), \(D=8\)) has exactly 128.

## Assumptions and scope
Here a minimal component is a nonempty closed shift-invariant subset on which the bilateral shift is minimal; its fibre rank is the cardinality of its intersection with every inverse-image fibre. Only binary alphabets and dyadic offsets \(D=2^r\) with \(r\ge2\) are claimed. A choice of an initial word \(u=(x_0,\ldots,x_{D-1})\in\{0,1\}^{D}\), together with a base point \(y\in Y\), determines the complete bilateral preimage uniquely by \(x_{j+D}=x_j+y_j\pmod2\) in both temporal directions. Thus every fibre has size \(2^D\). The substitution is primitive, hence \(Y\) is minimal and the same finite language appears throughout \(Y\).

## Proof
**1. The substitution's arithmetic skeleton.** Let \(t=(t_j)_{j\ge0}\) denote the one-sided fixed point beginning in \(1\). Since \(\vartheta(z)_{2m}=1\) and \(\vartheta(z)_{2m+1}=1-z_m\), we have
\[
t_{2m}=1,\qquad t_{2m+1}=1-t_m,\qquad
 t_j=1-\bigl(\nu_2(j+1)\bmod2\bigr),
\]
where \(\nu_2\) is the exponent of two in a positive integer. For every integer \(n\ge2\), let \(w_n=t_0\cdots t_{2^n-2}\), of length \(2^n-1\), and let \(B=2^{n-1}\).

We first determine **all** positive positions at which \(w_n\) occurs in \(t\). Suppose \(s>0\) and \(a=\nu_2(s)<n-1\). Taking the word position \(j=2^{a+1}-1\) gives \(\nu_2(j+1)=a+1\), but \(\nu_2(s+j+1)=a\), so \(t_{s+j}\ne t_j\). Hence any occurrence position must be a multiple \(s=Bk\). At these positions, the valuation comparison agrees automatically for \(j+1\ne B\) in \(1\le j+1<2B\). At the single exceptional index \(j+1=B\), equality holds precisely when \(\nu_2(k+1)\) is even. Since \(t_k=1\) exactly under that condition, the exact occurrence set, including the origin, is
\[
\bigl\{Bk:k\ge0,\ t_k=1\bigr\}.
\]
Every even-indexed symbol \(t_{2m}\) equals one. Therefore consecutive occurrences have displacement \(L=B\) or \(L=2B\). Equivalently, if they begin at \(Bk\) and \(B(k+e)\), then \(e\in\{1,2\}\), \(t_k=t_{k+e}=1\), and in the case \(e=2\) one has \(t_{k+1}=0\). These same return words are valid throughout \(Y\) because \(t\) generates the primitive substitution language.

**2. Every sufficiently refined return flips exactly one fibre bit.** Fix \(r\ge2\), let \(D=2^r\), and choose any \(n\ge r+2\). Then the return lengths above are multiples of \(D\), and \(L/D\) is even. If \(x_{j+D}=x_j+t_j\pmod2\), the change in its \(D\)-letter prefix between consecutive occurrences starting at \(s=Bk\) and \(s+L\) has coordinate
\[
\Delta_j=\sum_{h=0}^{L/D-1}t_{s+j+hD}\pmod2,
\quad 0\le j<D.
\]
For \(0\le j<D-1\), all summands have the same \(2\)-adic valuation \(\nu_2(j+1)<r\) in their index plus one. They are constant binary symbols, and their number is even. Thus \(\Delta_j=0\).

For the final coordinate \(j=D-1\), put \(C=B/D=2^{n-1-r}\), which is even. The symbol \(t_{s+D-1+hD}\) equals either \(t_{Ck+h}\) or its binary complement, according to the parity of \(r\); the complement has no effect on an even-length sum. The elementary block-parity identity
\[
\sum_{h=0}^{2^q-1}t_{2^q k+h}\equiv t_k\pmod2\qquad(q\ge0)
\]
follows by repeatedly pairing \(t_{2m}+t_{2m+1}\equiv t_m\pmod2\). Consequently
\[
\Delta_{D-1}=\sum_{h=0}^{Ce-1}t_{Ck+h}\equiv
\sum_{a=0}^{e-1}t_{k+a}\equiv1\pmod2.
\]
The last equality uses \(t_k=1\), and \(t_{k+1}=0\) when \(e=2\). Hence **every** first return to the cylinder defined by \(w_n\), for every \(n\ge r+2\), acts on the \(D\)-letter fibre by translation by the last unit vector \(e_{D-1}\in\mathbb F_2^D\). This is an infinite-word calculation, not an inference from sampled return times.

**3. A reference fibre and its orbit closures.** Construct a bilateral point \(y_*\in Y\) by taking a limit of the translates \(\sigma^{2^{2m}}\tilde t\), where \(\tilde t\in Y\) is any bilateral extension of \(t\). Directly from the valuation formula, the coordinatewise limit exists and satisfies
\[
(y_*)_j=1-\bigl(\nu_2(|j+1|)\bmod2\bigr)\quad(j\ne-1),
\qquad (y_*)_{-1}=1.
\]
Its nonnegative coordinates form \(t\). For every increasing sequence of sufficiently large **even** integers \(n\), one has \(\sigma^{2^n}y_*\to y_*\): the only exceptional coordinate is \(j=-1\), at which \(\nu_2(2^n)=n\) is even. The first positive return of \(t\) to \(w_n\) begins at \(2^n\), because \(t_0=1\), \(t_1=0\) and \(t_2=1\).

For each prefix \(u\in\mathbb F_2^D\), let \(x_u\in\eta_D^{-1}(y_*)\) be its uniquely determined bilateral lift, and let \(M_u\) be its forward orbit closure. By Step 2 and the convergence just proved, the sequence \(\sigma^{2^n}x_u\), along even \(n\to\infty\), converges to \(x_{u+e_{D-1}}\). The same argument starting from \(u+e_{D-1}\) yields the reverse inclusion of orbit closures, so
\[
M_u=M_{u+e_{D-1}}.
\]
Conversely, any forward orbit iterate tending to the reference fibre over \(y_*\) must, once sufficiently near it, begin with the word \(w_{r+2}\). Such times are concatenations of first returns to that word. By Step 2 their fibre action is a power of translation by \(e_{D-1}\). Consequently
\[
M_u\cap\eta_D^{-1}(y_*)=\{x_u,x_{u+e_{D-1}}\}.
\]
To prove \(M_u\) is minimal, take any nonempty minimal subset \(N\subseteq M_u\). Its image under \(\eta_D\) is a nonempty closed invariant subset of the minimal base \(Y\), hence all of \(Y\). Therefore \(N\) meets the fibre over \(y_*\). By the displayed identity, it contains one of \(x_u,x_{u+e_{D-1}}\); the forward orbit closure of either is \(M_u\). Since \(N\) is closed and forward invariant, \(N=M_u\). Thus every \(M_u\) is a minimal component.

**4. Constant ranks and exhaustion.** Distinct minimal sets cannot intersect. The displayed reference-fibre formula therefore shows that there are precisely \(2^{D-1}\) pairwise distinct sets \(M_u\), one for each pair \(\{u,u+e_{D-1}\}\).

For completeness, fibre rank of a minimal component is constant. If a component \(M\) contains \(a\) distinct points over \(y\in Y\), choose positive shift times sending \(y\) arbitrarily close to any prescribed \(z\in Y\). Compactness gives \(a\) limiting points in \(M\) over \(z\). They remain distinct because a shift induces a **permutation** on the finite set of \(D\)-letter prefixes, so distinct points over the same base remain separated somewhere in their first \(D\) coordinates. Hence \(\#M_y\le\#M_z\); interchanging \(y\) and \(z\) gives equality. Every \(M_u\) therefore has rank two over every \(y\in Y\). The \(2^{D-1}\) disjoint minimal components already account for \(2^{D-1}\cdot2=2^D\) points over each \(y\), which is the entire lift fibre. Their union is thus \(X_D\) and there are no additional minimal components. This proves the theorem.

## Verification
The proof is an all-parameter argument in the integers \(r\ge2\) and \(n\ge r+2\). Its critical identities are the exact occurrence classification, the block-parity identity, the single-coordinate return translation, the reference-fibre orbit-closure comparison, and constant fibre rank. Run `python3 check_dyadic_pd_lifts.py` with Python 3 and no nonstandard dependencies. The script independently constructs the substitution word, checks it against the valuation formula, locates occurrences by direct substring search, and verifies each binary return-coordinate sum. It checked 20,106 first-return intervals for \(r=1,2,3,4\) and admissible \(n\le9\), with no mismatches. These finite computations only stress-test the infinite proof.

## Relationship to prior work
Kang and Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes* (arXiv:2609.01140v1, first posted 2026-09-01), Theorem 1.7 and Propositions 4.9–4.10, prove that the binary lifts with odd block length at least five are **non-minimal**. Their general decomposition results imply finitely many minimal subsets and constant fibre ranks, but do not specify counts or ranks for the dyadic block lengths \(2^r+1\), \(r\ge2\). Their precise three-block case has a different offset and is not covered by the present theorem.

The published mathematical finding *Exact component and fibre-rank law for the three-block period-doubling lift* (2026) classifies the three-symbol difference code at all alphabet moduli. In its binary instance it gives two components of rank two, and explicitly excludes larger odd block lengths from its scope. The identity \(\eta_{2^r}=(I+\sigma)^{2^r}\) over \(\mathbb F_2\) relates the constructions algebraically, but knowing the decomposition for one application does **not** determine the components of repeated inverse images. The new return-permutation identity above is the step needed to calculate the complete family.

## Limitations
The formula is not asserted for non-dyadic offsets, larger alphabets, other substitutions, invariant-measure simplices, or spectral invariants. No claim of uniqueness against all conceivable equivalent odometer descriptions is made. The published source comparison leaves a residual risk that older work on finite odometer or Toeplitz group extensions expresses this same family in different terminology. Independent scientific validation has not been performed.

## References
1. Zeyu Kang and Tobias Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1 (submitted 2026-09-01), https://arxiv.org/html/2609.01140 .
2. *Exact component and fibre-rank law for the three-block period-doubling lift*, public mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-component-and-fibre-rank-law-for-the-three-block-period-do--a7e0bd7bb899 .
