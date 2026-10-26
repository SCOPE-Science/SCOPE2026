# Preconditional spectra on finite height-two lattices

## Finding
For every integer \(m\ge3\), write \(M_m=\{0,1,a_1,\dots,a_m\}\) for the lattice with bottom \(0\), top \(1\), and \(m\) pairwise incomparable atoms. The numbers of preconditional operations satisfying the successive axioms of \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\), respectively, are
\[
K_m=(m+3)^m+2^m+2m3^{m-1},\qquad T_m=m^m,\qquad F_m=\sum_{k=0}^{\lfloor m/2\rfloor}\frac{m!}{2^k k!(m-2k)!}.
\]
Every \(\mathsf F\)-operation corresponds uniquely to a partial matching of the labelled atoms. The involutive-negation cases correspond precisely to perfect matchings and, by Holliday's Sasaki characterization, to ortholattice Sasaki hooks.

## Assumptions and scope
A **preconditional** is a binary operation \(\to\) on a bounded lattice satisfying for all \(x,y,z\):

1. \(1\to x\le x\).
2. \(x\wedge y\le x\to y\).
3. \(x\to y\le x\to(x\wedge y)\).
4. \(x\to(y\wedge z)\le x\to y\).
5. \(x\to((x\wedge y)\to z)\le (x\wedge y)\to z\).

These are the five axioms of Holliday's preconditionals, in Chen's notation. A \(\mathsf T\)-preconditional also satisfies \(x\to x=1\) and \(x\wedge(x\to0)=0\). A \(\mathsf F\)-preconditional additionally satisfies \(x\le(x\to0)\to0\). The lattice carrier, all atoms, and the binary operation are fixed/labelled; counts are of distinct operations, not atom-permutation isomorphism classes.

## Proof
For each atom \(a_i\), set \(d=0\to0\), \(c_i=a_i\to0\), and \(t_i=a_i\to a_i\). Axioms 1 and 2 imply \(1\to x=x\). Axioms 3 and 4 imply \(0\to x=d\) for every \(x\). The same two axioms, using \(a_i\wedge a_j=0\) for \(j\ne i\), imply \(a_i\to a_j=c_i\) for \(j\ne i\), while \(a_i\to1=t_i\). Axiom 2 gives \(t_i\in\{a_i,1\}\), and axiom 4 gives \(c_i\le t_i\).

The only remaining restrictions from axiom 5 are (a) \(a_i\to c_i\le c_i\) and (b) \(a_i\to d\le d\). The first excludes exactly \(c_i=a_i,t_i=1\); the second couples the rows through \(d\). All other cases of axiom 5 are tautologies or follow from these: the consequent of its inner arrow is one of \(c_i,t_i\), and \(a_i\to t_i\le t_i\) always holds. Conversely, any \(d,c_i,t_i\) satisfying these restrictions defines an operation obeying all five axioms by direct substitution in the row table. Thus the normal form is both necessary and sufficient.

If \(d=1\), each atom row has \(2\) choices \((t_i=a_i,c_i\in\{0,a_i\})\) or \(m+1\) choices \((t_i=1,c_i\in\{0,1\}\cup\{a_j:j\ne i\})\). There are \((m+3)^m\) such operations. If \(d=0\), every \(c_i=0\), with two choices for \(t_i\), giving \(2^m\). If \(d=a_j\), its row has \(t_j=a_j\) and two choices of \(c_j\), whereas every other row has three choices: \((c_i,t_i)=(0,a_i),(0,1),(a_j,1)\). Summing over the \(m\) possible \(j\) gives \(2m3^{m-1}\), completing the formula for \(K_m\).

For \(\mathsf T\), conditional identity forces \(d=1\) and \(t_i=1\). Semicomplementation excludes \(c_i=1\), and axiom 5 already excludes \(c_i=a_i\). Thus independently for every atom \(a_i\), the value \(c_i\) is either \(0\) or some different atom, giving exactly \(m^m\) operations.

For \(\mathsf F\), put \(N(x)=x\to0\). We have \(N(0)=1\), \(N(1)=0\), and \(N(a_i)=c_i\). If \(c_i=0\), double-negation inflation holds at \(a_i\) since \(N^2(a_i)=1\). If \(c_i=a_j\ne a_i\), it demands \(a_i\le N(a_j)=c_j\), forcing \(c_j=a_i\). Thus the nonzero values of \(c_i\) are disjoint two-cycles and all remaining atoms map to zero. Conversely every partial matching gives a unique operation in \(\mathsf F\). Choosing the \(2k\) matched atoms and pairing them yields \(m!/(2^k k!(m-2k)!)\) choices.

Lastly \(N^2(a_i)=a_i\) for every atom exactly when no atom is unmatched. Thus \(N\) is involutive exactly for perfect matchings (necessarily \(m\) even). The Sasaki-hook identification follows from Holliday's characterization of semicomplemented preconditionals with involutive negation.

## Verification
The accompanying standalone `checker.py` constructs candidates for the entire operation table and directly evaluates all five axioms, conditional identity, semicomplementation and double-negation inflation. It independently verifies the predicted triples for \(m=2,3,4\): \((41,4,2)\), \((278,27,4)\), \((2633,256,10)\). The proof handles all \(m\ge3\); finite tests are corroboration, not an infinite proof. To rerun use `python3 checker.py`.

## Relationship to prior work
Chen (2026) formulates the three \(\mathsf K\subseteq\mathsf T\subseteq\mathsf F\) classes and proves general semantic results, not this labelled height-two operation census. Holliday (2024/2025) provides the preconditional axioms and the Sasaki characterization for involutive negation, and explicitly studies one modular height-two ortholattice as an example. The present claim is a full normal form and enumeration across all \(m\ge3\), including non-involutive \(\mathsf F\) operations. Previous finite-chain classifications apply to a different lattice order and do not imply these expressions.

## Limitations
The count assumes exactly one bottom, one top, and \(m\) incomparable named atoms; it is not a count of arbitrary finite lattices or operations modulo automorphisms. Generic relational representation and involutive Sasaki facts are credited as prior work. Independent verification and a universal priority search have not been performed.

## References
- Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221 (first posted 2026-07-22), especially Definitions 3.1 and 3.3.
- Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296 (first posted 2024-02-03), especially Definition 1 and Proposition 4.
