# Quantifier-rank and variable-width transfer through generalized dihedral groups

## Finding
Let \(A,B\) be arbitrary (finite or infinite) abelian groups in which \(2a=0\) implies \(a=0\). Equip them with equality, a named zero, and the ternary relation \(T(a,b,c)\) meaning \(a+b=c\). Write \(\operatorname{Dih}(A)=A\rtimes C_2\) for the inversion semidirect product, represented as pairs \((a,i)\) with \(i\in\{0,1\}\), whose multiplication is
\[
(a,i)(b,j)=(a+(-1)^i b,\ i+j\pmod 2).
\]
Equip these groups with equality, a named identity and a ternary relation \(M(x,y,z)\) meaning \(xy=z\). For every quantifier rank \(q\ge0\) and every variable bound \(k\ge0\), the following are equivalent:
\[
(A;0,T)\equiv^{\mathrm{FO}^k}_q(B;0,T)
\quad\Longleftrightarrow\quad
(\operatorname{Dih}(A);e,M)\equiv^{\mathrm{FO}^k}_q
(\operatorname{Dih}(B);e,M).
\]
Here \(\mathrm{FO}^k\) permits reuse of at most \(k\) distinct variable names and \(\equiv_q\) means agreement on every sentence of quantifier rank at most \(q\). In particular, the least distinguishing rank in each finite-variable fragment, taking infinity if no such sentence exists, is identical on both sides. The statement includes every finite abelian group of odd order as well as all torsion-free abelian groups.

## Assumptions and scope
The hypothesis excluding nonzero elements of order two is used for one direction: the canonical abelian subgroup must be definable without quantifiers in the generalized dihedral group. The opposite direction, lifting equivalence of abelian groups to their inversion semidirect products, works for every abelian group, including groups with two-torsion. The proof concerns relational multiplication with a named identity, not a language with binary function symbols. The statement is about unrestricted Boolean first-order formulas with a quantifier-rank and variable-name budget; it does not claim any new classification of individual finite abelian groups.

## Proof
**Step 1: a uniform quantifier-free translation of atoms.** Fix an assignment of parity bits \(\epsilon_x\in\{0,1\}\) to all free variables \(x\) of a group formula. Replace each variable interpreted as \((a_x,\epsilon_x)\) by an abelian-group variable \(a_x\) with the *same variable name*. The identity is \((0,0)\). An equality between two pairs becomes either an identically false formula, if their parity bits differ, or the equality of their coordinates. Equality to identity is handled analogously. An atom \(M(x,y,z)\) becomes false if \(\epsilon_x+\epsilon_y\not\equiv\epsilon_z\pmod2\). Otherwise it becomes \(T(a_x,a_y,a_z)\) if \(\epsilon_x=0\), and \(T(a_z,a_y,a_x)\) if \(\epsilon_x=1\), because \(a_x-a_y=a_z\) is equivalent to \(a_z+a_y=a_x\). Constants in any argument are replaced by zero. No new variables or quantifiers are introduced in these atomic translations.

Extend the translation by Boolean connectives. For a quantified variable \(x\), whose parity has not yet been fixed, use
\[
(\exists x\,\varphi)^* =
 (\exists x\,\varphi^*_{\epsilon_x=0})\ \lor\
 (\exists x\,\varphi^*_{\epsilon_x=1}),
\]
and the analogous conjunction of two universally quantified alternatives for \(\forall x\). Previously bound parity choices are handled by the ordinary recursive semantics of each subformula, including shadowing of variable names. Structural induction gives exact truth preservation under every variable assignment. By induction, the translated formula has quantifier rank at most the original rank and uses no variable name that the original did not use. Therefore agreement of \(A,B\) on \(\mathrm{FO}^k\) rank-\(q\) sentences implies agreement of their inversion semidirect products.

**Step 2: quantifier-free recovery of the kernel.** In \(\operatorname{Dih}(A)\), every element \((a,1)\) is an involution, since \((a,1)^2=(0,0)\). Every element \((a,0)\) other than the identity has square different from the identity: \((a,0)^2=(2a,0)\), and the two-torsion-free hypothesis forces \(2a\ne0\) when \(a\ne0\). Consequently the formula
\[
\delta(x):\quad (x=e)\ \lor\ \neg M(x,x,e)
\]
defines precisely \(A\times\{0\}\), without parameters or quantifiers. Restricting the group multiplication relation to this definable domain recovers \(T\) exactly. Relativize each quantifier of an abelian-group formula to \(\delta\): replace \(\exists x\,\varphi\) by \(\exists x\,(\delta(x)\land\varphi)\) and \(\forall x\,\varphi\) by \(\forall x\,(\delta(x)\Rightarrow\varphi)\). Again the quantifier rank and number of variable names do not increase. Therefore agreement of the generalized dihedral groups implies agreement of their abelian kernels at precisely the same rank and width. Combine Steps 1 and 2.

**Step 3: exact distinguishing rank.** The two implications hold at every \(q,k\), so the sets of ranks at which a sentence in \(\mathrm{FO}^k\) can distinguish the respective pairs coincide. Taking minima proves the asserted exact transfer, including infinity.

## Verification
The translation has two algebraic identities to check: multiplication in the parity-zero and parity-one cosets, and the square of each coset. Both follow by direct evaluation of the displayed semidirect-product multiplication. An executable exhaustive spot-check over three finite odd abelian kernels is supplied in `check_transfer_atoms.py`; its role is to check implementation of the displayed atomic identities, not to replace the universal induction proof. The proof does not use probabilistic computation, finite extrapolation or an unproved enumeration.

## Relationship to prior work
Gomaa's 2007 dissertation, Section 3.8, Lemma 3.10, already proves rank-\(q\) equivalence transfer between finite cyclic groups \(\mathbb Z/m\mathbb Z\) and ordinary dihedral groups of order \(2m\), for all positive moduli, relying partly on a 2000 manuscript by Koponen and Luosto. That **cyclic case is not claimed as new**. The present statement concerns arbitrary possibly noncyclic, possibly infinite abelian groups with no two-torsion; it also preserves every finite-variable fragment \(\mathrm{FO}^k\), using explicit rank- and width-preserving translations in both directions. The 2010 paper by Gomaa describes descriptive-complexity bounds for finite abelian groups and dihedral applications, but the accessible full dissertation's cited cyclic lemma is narrower than this statement. Preservation of variable width matters when transferring finite-pebble-game bounds to nonabelian group families. General logical facts about quantifier-free interpretations provide a method, but by themselves do not identify the quantifier-free canonical kernel or the precise inversion-doubling transfer.

## Limitations
The no-two-torsion assumption is essential to the *displayed* quantifier-free kernel formula; this work does not establish failure of every possible rank-preserving reduction when the kernel has two-torsion. The group signatures include a named identity and use ternary multiplication, so resource statements cannot automatically be transplanted to function-symbol group languages or languages without the identity constant. No uniqueness or historical priority is established against all unpublished work. In particular, the Koponen–Luosto manuscript referenced by Gomaa could not be inspected in full. The result is a structural transfer theorem, not a new numerical bound or an independent certification.

## References
1. W. Gomaa, *Model Theory and Complexity Theory*, University of Maryland dissertation (public repository date 2007-07-06), Sections 3.1 and 3.8, especially Lemma 3.10. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116. https://doi.org/10.1142/S0218196710006047
3. A. Koponen and K. Luosto, *Definability of Group Theoretic Notions*, manuscript (2000), cited as reference [19] in Gomaa (2007); full text unavailable for inspection.
