# Independent mathematical audit

## correctness

PASS

Reconstructed all definitions from actual RESULT.md and primary Tran arXiv:2610.01216v1: N=6, q_ii=1, q_ij in (1,2), H=phi[K], phi(x)=(3x-x^3)/2, T=(C+2)/8, and circulant equations (15),(16). Independent SymPy exact radical simplification established A^2+2A-7=0, C^2+(2-A)C+A^2-4A+1=0, zero constant Fourier mode, h1=h3=4T(1-C)^2, h2=4T(1-2A+C)^2, each of four cyclic-distance E_m=0, and the full 6x6 matrix identity H=4TK(I-J/6)K. Strict inequalities follow rigorously since A in (3/2,2), the second quadratic is negative at 1 and positive at A=(2sqrt2-1), is increasing on [1,A], and C is its positive root; hence 1<C<A<2. T>0, 1-C!=0 and 1-2A+C<0 imply positive nonconstant H eigenvalues. Therefore H is PSD rank5 with positive kernel ones; Tran Theorem 2.3 and Lemma 9.1 give a real nondegenerate five-simplex with regular Morley simplex. Since A!=C it is nonregular. Independent exhaustive 720-permutation test of the two-valued K gives exactly 48 automorphisms and only the three matched-pair transpositions, which Tran Proposition 3.1 identifies as actual hyperplane reflections. Approximate H eigenvalues (0, .745166[x3], 1.882251[x2]) are corroboration, not the proof of positivity.

## originality

PASS

Full primary arXiv HTML v1 was read at Theorem 2.3, Proposition 3.1, Theorem 3.4, Sections 5–6, all of Section 9 including equations (15),(16), Lemma 9.1, Remark 9.2, Theorem 9.3 and Tables 1–2, plus Sections 11–12. The primary source explicitly states that no existence/nonexistence result is asserted for N=6,7,8; its n=5 examples are uncertified numerical observations; certified dihedral existence starts at N=9. The assessed theorem supplies the missing exact solution at N=6 together with a full 48-element symmetry group, not merely the known conditional implication. Fresh Resultary and web searches under six-vertex, dihedral, two-distance matching, Morley, and radical aliases did not reveal independent prior equivalent coverage; the closest other published record treats only the formal continuous-limit equation, whose Fourier conditions cannot imply this finite solution. This is a best-of-knowledge PASS with specific priority risk from very recent unindexed follow-ups and the known prior numerical examples.

## value

PASS

Dimension five is singled out by Tran’s still-open G5 two-disjoint-reflections conjecture, while the N=6 dihedral existence case is explicitly left untreated and the known examples are numerical. An exact closed-form nonregular five-simplex with regular Morley simplex is a natural substantive finite existence result, not an arbitrary parameter evaluation: it supplies an exact benchmark for the new Morley regularity equations and identifies the complete order-48 isometry group and all three reflection transpositions. The radical certificate replaces reported numerical evidence with an exact analytic construction for one symmetry family. It has clear use in comparing potential dimension-five classifications and testing conjectured symmetry restrictions; neither universal G5 proof nor full N=6 classification is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
