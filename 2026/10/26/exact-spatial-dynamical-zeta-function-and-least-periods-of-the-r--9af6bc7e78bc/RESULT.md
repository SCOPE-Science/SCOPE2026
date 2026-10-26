# Exact spatial dynamical zeta function and least periods of the Rule 110 one-step image

## Finding
Let \(F_{110}:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be the elementary cellular automaton of Wolfram Rule 110, and let \(Y=F_{110}(\{0,1\}^{\mathbb Z})\), equipped with the **spatial** shift \(\sigma\). For each integer \(n\ge1\), put
\[
P_n=\#\{y\in Y:\sigma^n y=y\}.
\]
Then the spatial Artin--Mazur zeta function is exactly
\[
\boxed{\zeta_Y(z)=\exp\!\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right)
=\frac{1-z-z^4}{(1-z)(1-2z+z^2-z^3-z^4)}.}
\]
The initial spatial fixed-point counts are \(P_1=2\), \(P_2=2\), \(P_3=5\), \(P_4=10\), \(P_5=22\), and \(P_6=41\). The set of **least** spatial periods occurring in \(Y\) is exactly
\[
\boxed{\{1\}\cup\{n\in\mathbb Z:n\ge3\}.}
\]
Equivalently, there are no primitive spatial period-two orbits, whereas a primitive orbit of every length at least three exists. The formula counts output configurations, not their possibly multiple input preimages and not the time-periodic points of \(F_{110}\).

## Assumptions and scope
Rule 110 is defined by \((F_{110}x)_i=f(x_{i-1},x_i,x_{i+1})\), where \(f(a,b,c)\) is bit \(4a+2b+c\) of integer 110. Thus \(f=1\) for neighborhoods `001`, `010`, `011`, `101`, and `110`, and \(f=0\) for `000`, `100`, and `111`. Every \(y\in Y\) has a bi-infinite antecedent, but its spatial period need not equal the spatial period of its antecedent. The spatial shift, rather than the time evolution, acts on \(Y\) in the zeta function above. All identities are exact formal power-series identities over the rational numbers.

## Proof
**1. Four-state predecessor graph.** Label its vertices by the two-bit words \(00,01,10,11\), indexed \(0,1,2,3\). For each triple \(abc\) insert an arrow \(ab\to bc\) labeled by \(f(a,b,c)\). Encode a Boolean relation as the sixteen-bit integer with bit \(4i+j\) set precisely when vertex \(i\) has an arrow or path to vertex \(j\). The two one-symbol relations are
\[
R_0=\texttt{0x8101},\qquad R_1=\texttt{0x42c2},
\]
and the identity relation is \(I=\texttt{0x8421}\). Products are Boolean relational products.

For any nonempty binary word \(w=w_1\cdots w_n\), its infinite periodic repetition \(w^\infty\) lies in \(Y\) **if and only if** the relation \(R_w=R_{w_1}\cdots R_{w_n}\) contains a directed cycle. Indeed, a cycle of \(k\) edges in \(R_w\) concatenates to a predecessor of spatial period dividing \(kn\). Conversely, a bi-infinite predecessor of \(w^\infty\) gives a bi-infinite walk, sampled at multiples of \(n\), in the finite graph \(R_w\); some directed cycle must exist. Every cycle-containing directed graph on four vertices has a cycle of length \(1,2,3\), or \(4\), so this criterion is decided by the four diagonal tests \(\operatorname{diag}(R_w^k)\ne0\), \(1\le k\le4\). This argument makes no assumption of an antecedent of period \(n\).

**2. The complete finite transfer certificate.** Starting at \(I\), repeatedly multiply on the right by \(R_0\) and \(R_1\), retaining every distinct Boolean relation. Breadth-first closure contains **exactly 75 relations**. Let \(T\) be the 75-state integer transition matrix whose \((s,t)\)-entry is the number (zero, one, or two) of binary labels taking state \(s\) to state \(t\). Let \(v(s)=1\) if relation \(s\) contains a directed cycle, and \(v(s)=0\) otherwise. Let \(u\) select the initial identity relation. Then
\[
P_n=uT^nv\quad(n\ge1),\qquad uT^0v=1.
\]
The standalone integer verifier reconstructs every state and edge from the eight entries of Rule 110. Its crucial exhaustive certificate is the **75-coordinate vector identity**
\[
\bigl(T^9-4T^8+6T^7-5T^6+T^5+4T^4-4T^3+2T^2-I\bigr)v=0.
\]
This is checked at every reachable relation by exact integer arithmetic, not guessed from finitely many scalar counts. Multiplying on the left by \(uT^n\) establishes the resulting order-nine recurrence for **every** \(n\ge0\).

**3. Rational functions.** Set \(P_0=1\) as an algebraic convention and \(G(z)=\sum_{n\ge0}P_nz^n\). The vector identity and the first nine values, also computed by the finite transfer system, give
\[
G(z)=\frac{1-2z+4z^3-7z^4+8z^5-6z^6+4z^7}
{(1-z)(1-z-z^4)(1-2z+z^2-z^3-z^4)}.
\]
For \(A(z)=1-z-z^4\) and \(B(z)=(1-z)(1-2z+z^2-z^3-z^4)\), exact polynomial multiplication verifies
\[
\frac{G(z)-1}{z}=\frac{A'(z)}{A(z)}-\frac{B'(z)}{B(z)}.
\]
Since \(A(0)=B(0)=1\), formal integration of the logarithmic derivative yields \(\zeta_Y(z)=A(z)/B(z)\), exactly as claimed.

**4. Least-period spectrum.** The length-two periodic words `01` and `10` fail the directed-cycle criterion, whereas `00` and `11` satisfy it. Hence \(P_2=2\), and no least period two is possible. For each \(n\ge3\), the word \(w_n=1^{n-1}0\) has precisely one zero per cycle and therefore has least period exactly \(n\). To prove admissibility uniformly, calculate the first five powers of \(R_1\): the relations \(R_1^kR_0\) have diagonal entries for \(k=2,3,4,5\), and \(R_1^5=R_1^6\), so the latter property holds for every \(k\ge2\). Each \(w_n^\infty\) is thus in \(Y\). Both constant configurations occur, establishing least period one.

## Verification
Run `python3 verify.py` using Python 3 without external dependencies. The checker recomputes the two labeled relations, their complete 75-state closure, all directed-cycle predicates, all 75 coordinates of the ninth-degree annihilating polynomial, and the exact polynomial identity converting the periodic-point series into the zeta function. A separate bit-parallel implementation directly enumerates spatially periodic antecedents of periods \(n,2n,3n,4n\) for \(1\le n\le5\), checking the first five periodic-point counts. It also checks stabilization of the explicit primitive-period witnesses. All certificates are integer or Boolean calculations. The finite initial counts alone do not establish the universal recurrence; the checked vector identity does.

## Relationship to prior work
Nordahl (1989) proves regularity of finite-time languages of cellular automata and discusses finite-lattice **temporal** periodic sets; these are distinct from the spatial periodic points of the one-step image counted here. Cook (2004) establishes Rule 110 universality via spacetime gliders and does not supply this spatial-image zeta function. Manada and Kashyap (2009) explain a general zeta-function method for periodic-finite-type shifts, and Inoue and Krieger (2010) study zeta functions for coded systems involving Dyck shifts; the generic rationality of sofic-shift zeta functions is classical. The claim here is the **particular evaluated rational function and complete least-spatial-period spectrum** for the Rule 110 one-step image, not rationality in general or the known time dynamics. Spatial finite-word complexity and spatial periodic-point counts are distinct invariants; determining one generating function does not, by itself, determine the other.

## Limitations
Only the one-step image \(Y=F_{110}(\{0,1\}^{\mathbb Z})\) and its **spatial** shift are considered. The theorem does not count points periodic under iterations of \(F_{110}\), does not classify temporal limit sets, and does not assert that every spatial-periodic output has an antecedent of the **same** period. Previous use of equivalent graph presentations could conceivably yield the same rational function implicitly; exhaustive historical priority is not certified. Formal proof of the unrestricted recurrence depends on reproducing the 75-state finite integer identity from the supplied checker.

## References
- Mats G. Nordahl, *Formal Languages and Finite Cellular Automata*, Complex Systems 3 (1989), 63–78. https://content.wolfram.com/sites/13/2018/02/03-1-5.pdf
- Matthew Cook, *Universality in Elementary Cellular Automata*, Complex Systems 15 (2004), 1–40. https://wpmedia.wolfram.com/uploads/sites/13/2018/02/15-1-1.pdf
- Akiko Manada and Navin Kashyap, *The Zeta Function of a Periodic-Finite-Type Shift*, arXiv:0904.2375v1 (15 April 2009). https://arxiv.org/abs/0904.2375
- Kokoro Inoue and Wolfgang Krieger, *Subshifts from Sofic Shifts and Dyck Shifts, Zeta Functions and Topological Entropy*, arXiv:1001.1839v1 (12 January 2010). https://arxiv.org/abs/1001.1839
