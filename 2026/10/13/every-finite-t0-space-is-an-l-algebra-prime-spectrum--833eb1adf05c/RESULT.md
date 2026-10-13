# Every finite T0 space is an L-algebra prime spectrum

## Finding
Let \(T\) be any finite \(T_0\)-space, possibly empty. Put the specialization order on its points in the convention
\[
x\le_T y \quad\Longleftrightarrow\quad \text{every open set containing }x\text{ also contains }y.
\]
Adjoin one new greatest element \(1\) and write
\[
\Omega=T\sqcup\{1\},\qquad t<1\quad(t\in T).
\]
Define
\[
x\cdot y=
\begin{cases}
1,&x\le y,\\
y,&x\not\le y.
\end{cases}
\]
Then \(\Omega\) is a finite \(L\)-algebra and
\[
\boxed{\operatorname{Spec}\Omega\cong T.}
\]
More explicitly, for each \(t\in T\),
\[
P_t:=\Omega\setminus\downarrow t
\]
is a prime ideal, every prime ideal is uniquely of this form, and the map \(t\mapsto P_t\) is a homeomorphism. Thus every finite \(T_0\)-space on \(n\) points is realized as the prime spectrum of an \(L\)-algebra on exactly \(n+1\) underlying elements.

## Assumptions and scope
Rump and Vendramin prove that if a partially ordered set \(\Omega\) has a greatest element \(1\), then the displayed operation makes \(\Omega\) an \(L\)-algebra and its ideals are exactly its nonempty upper sets. They also define \(\operatorname{Spec}X\) as the set of prime ideals of an \(L\)-algebra \(X\), with open sets
\[
U_I=\{P\in\operatorname{Spec}X:I\not\subseteq P\},
\]
and prove that spectra of arbitrary \(L\)-algebras are sober \(T_0\)-spaces with a basis of quasi-compact opens.

The present statement is the converse realization result restricted to finite \(T_0\)-spaces. No claim is made that the \(n+1\)-element realization is size-minimal, unique, functorial on all continuous maps, or valid without the \(T_0\) hypothesis. The empty space is included: adjoining one point gives the one-element \(L\)-algebra, whose spectrum has no proper prime ideals.

## Proof
Because \(T\) is finite, its topology is Alexandrov: an arbitrary intersection of open sets is the intersection of finitely many distinct opens and is therefore open. With the specialization convention above, the open sets are exactly the upper sets of the partial order \((T,\le_T)\). The \(T_0\) assumption makes this specialization preorder antisymmetric.

Adjoin a greatest element \(1\) to obtain \(\Omega\). By the poset construction of Rump and Vendramin, \(\Omega\), with
\[
x\cdot y=1\text{ if }x\le y,\qquad x\cdot y=y\text{ otherwise},
\]
is an \(L\)-algebra, and its ideals are exactly the nonempty upper sets. Since \(1\) is greatest, these are equivalently the upper sets containing \(1\).

Fix \(t\in T\). The set
\[
P_t=\Omega\setminus\downarrow t
\]
is a nonempty proper upper set, hence a proper ideal. To prove it is prime, use the lattice characterization of primality. Suppose ideals \(I,J\) satisfy
\[
I\cap J\subseteq P_t
\]
but neither \(I\) nor \(J\) is contained in \(P_t\). Choose
\[
x\in I\cap\downarrow t,\qquad y\in J\cap\downarrow t.
\]
Since \(I\) and \(J\) are upper sets and \(x,y\le t\), we have \(t\in I\cap J\). But \(t\notin P_t\), contradicting \(I\cap J\subseteq P_t\). Thus \(P_t\) is prime.

Conversely, let \(P\) be any prime ideal and put
\[
D=\Omega\setminus P.
\]
Then \(D\) is a nonempty down-set and \(1\notin D\). Because \(D\) is finite, it has maximal elements. It can have only one. Indeed, if \(a\ne b\) are two maximal elements of \(D\), the ideals \(\uparrow a\) and \(\uparrow b\) are both not contained in \(P\). Yet
\[
(\uparrow a)\cap(\uparrow b)\subseteq P:
\]
otherwise an element of \(D\) would lie above both \(a\) and \(b\), contradicting maximality. This violates primality of \(P\). Hence \(D\) has a unique maximal element \(t\). Every point of a finite down-set lies below a maximal element, so
\[
D=\downarrow t,
\]
and therefore \(P=P_t\). This proves that \(t\mapsto P_t\) is a bijection from \(T\) to \(\operatorname{Spec}\Omega\).

It remains to identify the topology. Let \(I\) be any ideal of \(\Omega\). For \(t\in T\),
\[
\begin{aligned}
P_t\in U_I
&\Longleftrightarrow I\not\subseteq P_t\\
&\Longleftrightarrow I\cap\downarrow t\ne\varnothing\\
&\Longleftrightarrow t\in I.
\end{aligned}
\]
The last equivalence uses that \(I\) is an upper set. Therefore the inverse image of \(U_I\) under \(t\mapsto P_t\) is exactly
\[
I\cap T.
\]
As \(I\) ranges over the ideals of \(\Omega\), the sets \(I\cap T\) range over all upper sets of \(T\), hence over all opens of the original finite space. The bijection is therefore a homeomorphism.

## Verification
The accompanying exact replay enumerates every labeled poset on at most five points. For each one it adjoins a new greatest element, directly checks all \(L\)-algebra axioms for the poset operation, enumerates all ideals and all prime ideals, verifies
\[
\operatorname{Spec}\Omega=\{\Omega\setminus\downarrow t:t\in T\},
\]
and checks that every spectrum open pulls back to exactly the corresponding upper set of \(T\).

The replay independently recovers the known labeled-poset counts
\[
1,1,3,19,219,4231
\]
for cardinalities \(0,1,2,3,4,5\), and returns

```text
VERIFY_OK 1115466 exact assertions; 4474 labeled posets checked
```

Finite enumeration is corroborative only; the theorem is proved symbolically above.

## Relationship to prior work
Rump and Vendramin prove the general forward theorem that every \(L\)-algebra spectrum is a sober \(T_0\)-space with a quasi-compact-open basis. In the same paper they record the poset construction used here: a poset with greatest element becomes an \(L\)-algebra under the displayed implication operation, and its ideals are the upper sets. The inspected source does not state that adjoining one greatest point to an arbitrary finite \(T_0\)-space recovers that space exactly as the full prime spectrum.

Rump's earlier *L-algebras and topology* initiates the topological spectrum theory and treats classes whose ideals admit explicit descriptions. Targeted searches under finite-space, Alexandrov, poset, upper-set, and prime-spectrum formulations did not locate the finite realization theorem above. Semantic-index searches likewise returned finite-poset and finite-space results in other settings, but no equivalent \(L\)-algebra spectrum construction.

The proof also uses the standard elementary fact that a finite \(T_0\)-space is the Alexandrov space of its specialization poset. The new content claimed here is the exact combination of that finite-space correspondence with the published poset \(L\)-algebra construction and the classification of its prime ideals.

## Limitations
The realization is deliberately finite. Infinite \(T_0\)-spaces need not be Alexandrov, and even an infinite Alexandrov poset can have prime upper-set ideals whose complements are directed down-sets without a greatest point, so the same one-point argument does not automatically identify the spectrum with the original carrier.

The construction is not asserted to be canonical with respect to arbitrary continuous maps, nor is the added point proved necessary. The originality search was targeted rather than exhaustive. Because the proof is short once the two standard ingredients are juxtaposed, an equivalent observation could exist as folklore, in lecture notes, or under terminology not recovered by the searches. The accessible arXiv text is a later postprint revision; the source itself was first public in 2022 and appeared in the 2024 journal volume.

## References
1. W. Rump and L. Vendramin, *The prime spectrum of an L-algebra*, arXiv:2206.01001, first submitted 2 June 2022; *Proceedings of the American Mathematical Society* 152 (2024), 3197–3207, DOI 10.1090/proc/16802.
2. W. Rump, *L-algebras and topology*, *Journal of Algebra and Its Applications* 22 (2023), 2350034; published online 27 November 2021, DOI 10.1142/S0219498823500342.
