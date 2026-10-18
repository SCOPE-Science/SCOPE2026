# Congruence-rank spectrum and unary reconstruction of finite weak Heyting–Brouwer chains

## Finding
For every integer \(n\ge1\), let \(A_n\) be the fixed bounded chain of cardinality \(n+1\). A weak Heyting–Brouwer (WHB) expansion of \(A_n\) consists of strict implication \(\to\) and weak difference \(\leftarrow\) satisfying the four weak-Heyting, four weak-difference and two WHB interaction identities given below. Define \(\Box b=1\to b\). Then:

1. The map from WHB expansions to \(\Box\) is a bijection onto monotone, top-preserving maps \(A_n\to A_n\). Every such \(\Box\) has a unique left adjoint \(\Diamond\), given by \(\Diamond a=\min\{b\in A_n:a\le\Box b\}\); the full expansion is reconstructed by
   \[
   a\to b=\begin{cases}1,&a\le b,\\\Box b,&a>b,\end{cases}
   \qquad
   a\leftarrow b=\begin{cases}0,&a\le b,\\\Diamond a,&a>b.\end{cases}
   \]
   Thus the number of WHB expansions is \(\binom{2n}{n}\).
2. Every such expansion has a Boolean congruence lattice. If \(n\ge2\), the complete distribution of Boolean ranks is
   \[
   \#\{A:\operatorname{Con}(A)\cong B_r\}
   =\begin{cases}
   \binom{2n}{n}-2^{n-2},&r=1,\\
   2^{n-r-1},&2\le r\le n-1,\\
   1,&r=n,\\
   0,&\text{otherwise.}
   \end{cases}
   \]
   Here \(B_r\) is the Boolean lattice of all subsets of an \(r\)-element set; in particular, rank one means precisely two congruences, or simplicity. The middle range is empty when \(n=2\). For \(n=1\), both expansions have rank one.
3. In the uniform distribution on expansions with fixed \(n\ge2\), the probability of simplicity is
   \[
   1-\frac{2^{n-2}}{\binom{2n}{n}}
   =1-\frac{\sqrt{\pi n}}{4\cdot2^n}(1+O(n^{-1})).
   \]

## Assumptions and scope
The underlying chain is fixed and bounded, with \(0\) and \(1\). Weak implication satisfies, for all \(a,b,c\),
\[
a\to a=1,\quad a\to(b\wedge c)=(a\to b)\wedge(a\to c),\quad
(a\vee b)\to c=(a\to c)\wedge(b\to c),\quad
(a\to b)\wedge(b\to c)\le a\to c.
\]
Weak difference satisfies the order-dual identities
\[
a\leftarrow a=0,\quad (a\vee b)\leftarrow c=(a\leftarrow c)\vee(b\leftarrow c),\quad
a\leftarrow(b\wedge c)=(a\leftarrow b)\vee(a\leftarrow c),\quad
a\leftarrow c\le(a\leftarrow b)\vee(b\leftarrow c).
\]
The two compatibility identities are
\[
a\wedge((a\to b)\leftarrow0)\le b,
\qquad a\le b\vee(1\to(a\leftarrow b)).
\]
These are exactly the WHB identities of Celani, Nagy and Zuluaga Botero [1], Definition 4.3. No normality \(\Box0=0\), reflexivity, transitivity, or additional modal axioms are assumed.

## Proof
**Dual-chain normal form.** We use the WHB-frame duality in [1], Theorems 4.5 and 5.7. The finite Priestley dual of \(A_n\) is the increasing chain \(X=\{0,\ldots,n-1\}\), and an admissible frame consists of two relations \(R,S\) with \(S=R^{-1}\) and the prescribed order-composition conditions. From the WH condition, the rows \(R(i)\) shrink with increasing \(i\). From the WD condition applied to \(S\), each row \(R(i)\) is an upset in \(X\). Conversely these two conditions suffice, including the WHB interaction because \(S=R^{-1}\). Hence there is a unique nondecreasing threshold vector
\[
0\le t_0\le t_1\le\cdots\le t_{n-1}\le n,\qquad
R(i,j)\iff j\ge t_i,
\]
where \(t_i=n\) represents the empty row. Threshold vectors are weakly increasing length-\(n\) words over \(\{0,\dots,n\}\), so their total is \(\binom{2n}{n}\).

**Connective reconstruction.** Put \(U_i=\{i,\ldots,n-1\}\) for \(0\le i<n\), and \(U_n=\varnothing\). These are all elements of \(A_n=\operatorname{Up}(X)\), with top \(U_0\) and bottom \(U_n\). The frame operations [1] are
\[
U\Rightarrow_R V=\{x:R(x)\cap U\subseteq V\},\qquad
U\Leftarrow_{R^{-1}}V=\{y:\exists x\in U\setminus V\ (x,y)\in R\}.
\]
If \(i\ge j\), \(U_i\subseteq U_j\), and these give top and bottom respectively. If \(i<j\), then \(U_i\setminus U_j=[i,j-1]\) and monotonicity of thresholds gives
\[
U_i\Rightarrow_RU_j=U_{k_j},\qquad
U_i\Leftarrow_{R^{-1}}U_j=U_{t_i},
\qquad k_j=\min\{x:t_x\ge j\},
\]
with the empty minimum interpreted as \(n\). In particular \(\Box U_j=U_{k_j}\) and \(\Diamond U_i=U_{t_i}\). The equivalences
\[
\Diamond U_i\subseteq U_j\ \Longleftrightarrow\ t_i\ge j\ \Longleftrightarrow\ i\ge k_j\ \Longleftrightarrow\ U_i\subseteq\Box U_j
\]
prove \(\Diamond\dashv\Box\). A right adjoint on a finite chain is exactly a monotone top-preserving map. Conversely, given any such \(\Box\), its uniquely determined left adjoint \(\Diamond a=\min\{b:a\le\Box b\}\) yields the unique threshold vector and hence a WHB frame and expansion. Substituting into the displayed operations gives the reconstruction formulas in the finding.

**Congruence components.** By [1], Theorem 5.10, congruences correspond to subsets of \(X\) closed under both \(R\) and \(R^{-1}\). As \(X\) is finite and discrete, these are exactly unions of weakly connected components of the undirected graph underlying \(R\). Therefore \(\operatorname{Con}(A)\cong B_k\), where \(k\) is the number of these components.

If all thresholds equal \(n\), there are no edges, and \(k=n\). Otherwise let \(a=\#\{i:t_i<n\}\) and \(b=t_0\). The active rows are \(0,\dots,a-1\); the vertices incident as columns are exactly \(b,\dots,n-1\). Each active row has an edge to \(n-1\), and vertex \(0\) has an edge to every column \(j\ge b\). Thus \(\{0,\dots,a-1\}\cup\{b,\dots,n-1\}\) forms one connected component, and precisely the \(g=\max(0,b-a)\) vertices strictly between these intervals are isolated. Hence
\[
k=1+\max(0,b-a)\quad\text{for nonempty }R,
\qquad k=n\quad\text{for empty }R.
\]

**Rank enumeration.** Fix \(g\ge1\). We must have \(b=a+g\) and \(1\le a\le n-g-1\). With these \(a,b\) fixed, monotonicity and the fact that precisely the first \(a\) rows are nonempty leave
\[
\#\{t\}=\binom{n-g-2}{a-1}
\]
ways to choose \(t_1,\ldots,t_{a-1}\) in \([b,n-1]\), all subsequent thresholds being \(n\). Summing over \(a\) gives \(2^{n-g-2}\) for \(1\le g\le n-2\). There is exactly one empty relation, of Boolean rank \(n\). The number of nonsimple expansions is therefore \(\sum_{g=1}^{n-2}2^{n-g-2}+1=2^{n-2}\) for \(n\ge2\), and subtraction from \(\binom{2n}{n}\) gives the simplicity count. The \(n=1\) case has two relations and both yield one connected component. Stirling's formula \(\binom{2n}{n}=4^n(\pi n)^{-1/2}(1+O(n^{-1}))\) yields the asymptotic statement.

## Verification
Run the standalone standard-library Python program `python3 verify.py`. It enumerates all threshold vectors for \(1\le n\le7\), independently evaluates every defining identity on the resulting full operation tables, verifies the graph component count, and checks the rank distribution and totals. For \(1\le n\le4\), it also enumerates every convex chain congruence and directly checks compatibility with both binary operations. Finally, it exhausts all \(3^9=19683\) possible binary tables on the three-element chain to determine the admissible weak implication and weak difference tables and verifies that the complete WHB-pair set agrees with the six threshold constructions. The script prints `VERIFY_OK` on success. Finite checks are corroborative; the unrestricted theorem is proved above.

## Relationship to prior work
Celani, Nagy and Zuluaga Botero [1] establish the general WHB axiomatics, the dual-frame representation and the general congruence correspondence used as established inputs. They do not give the finite-chain threshold enumeration, unary recovery of both binary operations, the exact Boolean-congruence-rank distribution, or the asymptotic simplicity law. Alizadeh and Joharizadeh [2] give an algorithm to count *one-connective* weak Heyting expansions of finite distributive lattices, not the paired WHB operations with inverse relational compatibility; full inspection of [2] was unavailable, so priority risk remains. The classical sequence of central binomial coefficients [3] matches the *total counts* numerically; neither that identity nor the general frame duality by itself records the congruence-rank spectrum claimed here.

## Limitations
The classification concerns a fixed finite bounded chain and the stated weak WHB axioms, not arbitrary finite distributive lattices, the pure weak-Heyting reduct, or isomorphism classes across different underlying chain sizes. The proof relies on the published general WHB duality and congruence correspondence, whose statements were inspected in the primary manuscript; it does not reprove all of that duality. The originality assessment is a literature comparison rather than proof of historical priority; a coincidentally equivalent chain classification under Galois-connection or finite-relation terminology may exist. The earlier single-connective enumeration paper was accessible only through its abstract. Finite computations do not certify the asymptotic theorem independently.

## References
[1] Sergio Celani, Agustín Nagy and William Zuluaga Botero, *Bounded distributive lattices with strict implication and weak difference*, arXiv:2312.10873v1 (first public version 2023-12-18), especially Definitions 4.3–4.4, Theorems 4.5, 5.7 and 5.10; https://arxiv.org/abs/2312.10873 . Journal DOI: 10.1007/s00153-024-00945-2.

[2] Majid Alizadeh and Nima Joharizadeh, *Counting weak Heyting algebras on finite distributive lattices*, Logic Journal of the IGPL 23 (2015), 247–258, DOI: 10.1093/jigpal/jzu033 (abstract consulted).

[3] OEIS A000984, *Central binomial coefficients*, https://oeis.org/A000984 (numeric sequence only).
