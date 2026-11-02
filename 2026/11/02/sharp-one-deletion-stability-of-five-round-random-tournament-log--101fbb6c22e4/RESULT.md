# Sharp one-deletion stability of five-round random-tournament logic in Paley tournaments

## Finding
Let \(q\ge7\) be a prime power satisfying \(q\equiv3\pmod4\), and let \(T_q\) be the Paley tournament on \(\mathbb F_q\), with \(a\to b\) when \(b-a\) is a nonzero square. Let \(\mathcal R\) denote the countable random tournament, in the language of one directed-edge relation and equality. For any finite tournament \(T\), say that \(T\) has the **two-witness four-extension property** when, given four distinct vertices and any specified choices of edge direction between them and a new vertex, at least two distinct new vertices realize those choices.

**Theorem.** For every such \(q\), the following are equivalent:

1. \(q\ge107\).
2. \(T_q\) has the two-witness four-extension property.
3. For **every** vertex \(v\) of \(T_q\), the vertex-deleted tournament \(T_q-v\) agrees with \(\mathcal R\) on every first-order sentence of quantifier rank at most five.

The cutoff is sharp across **all** eligible prime powers. At \(q=107\), the least number of witnesses to a four-point orientation prescription is exactly two. By contrast, the Paley tournaments of orders \(67,71,79,83\) satisfy the ordinary (one-witness) four-extension property but fail the two-witness property; each has a deletion that fails the five-round theory of \(\mathcal R\).

## Assumptions and scope
A tournament has exactly one directed edge between any two different vertices. Throughout, \(\mathbb F_q\) is an arbitrary finite field of odd order \(q\equiv3\pmod4\). For a four-set \(A=\{a_1,a_2,a_3,a_4\}\), a sign vector \(\boldsymbol\epsilon\in\{\pm1\}^4\), and quadratic character \(\chi\) extended by \(\chi(0)=0\), define
\[
N_q(A,\boldsymbol\epsilon)=\#\{z\notin A:\chi(z-a_i)=\epsilon_i\ (1\le i\le4)\}.
\]
The two-witness property says \(N_q(A,\boldsymbol\epsilon)\ge2\) for every four-set and sign vector. Reversing every edge gives the same theorem, so the chosen orientation convention is immaterial. No counting quantifiers are present in the logical language.

## Proof
**1. Logical reduction.** For a finite tournament of at least seven vertices, agreement through quantifier rank five with the countable random tournament is equivalent to the ordinary four-extension property: the forward direction is given by its sixteen five-quantifier extension sentences, and the reverse direction by a five-round Ehrenfeucht–Fraïssé strategy (at most four vertices have already been chosen before any move). The property for four prescribed distinct vertices also supplies extensions of prescriptions on fewer vertices by padding them to four. Consequently, \(T-v\) has that five-round theory for every vertex \(v\) if and only if every four-set/orientation pattern in \(T\) has at least two witnesses. For the reverse implication, delete the sole witness of a pattern having exactly one, or delete a vertex outside its four-set when it has none.

**2. Finite prime-field calculation, with a rigorous symmetry reduction.** If \(p\equiv3\pmod4\) is prime, a translation followed by multiplication by a nonzero square is a tournament automorphism. Given a four-set, choose two distinct members \(a,b\) with \(b-a\) square (one of the two orders of any pair works, since \(-1\) is nonsquare). The automorphism \(z\mapsto(z-a)/(b-a)\) maps these members to \(0,1\). Thus an exact census of all \(\{0,1,x,y\}\), \(2\le x<y<p\), and all sixteen patterns proves an assertion for **all** four-sets. There are \((p-2)(p-3)/2\) normalized four-sets. The self-contained programs `verify.py` and `crosscheck.py` independently compute the minimum, by integer bitset intersections and by scalar character evaluation, respectively. Both examine every eligible prime \(7\le p\le211\). The minimum is at most one at each prime below \(107\); it equals two at \(107\), and is at least two at every eligible prime from \(107\) through \(211\). The exact per-prime minima and explicit attaining patterns are in `verification_output.json` and `crosscheck_output.json`. Because every pattern is tested after a proved orbit normalization, this is exhaustive finite verification, not random sampling.

**3. Uniform character bound.** For any odd prime power \(q\), write \(\chi\) for its quadratic character. For any distinct \(a_1,\dots,a_4\), expanding the character-product indicator gives
\[
16N_q(A,\boldsymbol\epsilon)=\sum_{z\notin A}\prod_{i=1}^4(1+\epsilon_i\chi(z-a_i)).
\]
The constant term contributes \(q-4\). Each of the four degree-one character sums is bounded in absolute value by \(3\), since its complete sum is zero and at most three nonzero summands have been omitted. Each of the six degree-two sums has absolute value at most \(3\): the complete sum is \(-1\), and at most two nonzero terms are removed. By the standard squarefree-polynomial quadratic-character Weil bound, each of the four degree-three sums has absolute value at most \(2\sqrt q+1\) after omission of the other member of \(A\), and the degree-four sum has absolute value at most \(3\sqrt q\). Therefore
\[
N_q(A,\boldsymbol\epsilon)\ge\frac{q-38-11\sqrt q}{16}.
\]
At \(q=223\) the right-hand side exceeds one, because \(169^2>121\cdot223\); the lower bound is increasing for \(q\ge223\). Thus every extension pattern has **at least two integer-valued witnesses** for all \(q\ge223\).

**4. Remaining prime powers.** If \(q\equiv3\pmod4\) is a nonprime prime power below \(223\), then \(q=27\) (or \(q=3\), excluded from the theorem). At \(q=27\), two witnesses for each of sixteen disjoint patterns on a fixed four-set would require at least \(32\) vertices outside the set, but only \(23\) exist. Thus \(q=27\) fails. All other eligible orders \(7\le q<223\) are the primes already exhaustively checked. Combining the finite census and the character bound proves the theorem.

## Verification
Run `python3 verify.py > verification_output.json` and `python3 crosscheck.py > crosscheck_output.json` with the Python standard library. These files are included in this package with exact output and byte hashes in the surrounding envelope. The programs use independent methods, agree on all twenty-four eligible primes through \(211\), and check \(\min N_{107}=2\). The uniform statement for \(q\ge223\) rests on the mathematical character-sum proof, not on finite extrapolation. The additional small nonprime case is excluded by an exact pigeonhole count.

## Relationship to prior work
Graham and Spencer introduced quadratic-residue tournament constructions and the character-sum method for domination extensions. Bonato, Gordinowicz and Prałat studied \(n\)-existentially closed tournaments and established ordinary four-extension at order \(67\). Javier, Llano and Zuazua discuss the ordinary \(P_3\) and \(P_4\) properties of Paley tournaments and associated neighborhood structures. A publicly available computational report identifies deletion criticality of the **common-dominator** property at order \(67\). These concern one witness, single-direction domination, or weaker extension properties, rather than the all-pattern **two-witness** cutoff and its five-round vertex-deletion interpretation. The new threshold is not a consequence of the one-witness statement: orders \(67,71,79,83\) demonstrate the difference.

## Limitations
This result concerns deletion of **one** vertex, four prescribed old vertices, five-round noncounting first-order logic, and Paley tournaments of prime-power order \(3\pmod4\). It does not claim the corresponding deletion robustness for arbitrary tournaments, larger deletion sets, or higher quantifier ranks. The uniform bound uses the classical Weil estimate for quadratic characters; the finite checks cover only the explicitly identified small prime fields. Historical priority has not been independently or exhaustively established.

## References
- R. L. Graham and J. H. Spencer, *A Constructive Solution to a Tournament Problem*, Canadian Mathematical Bulletin **14** (1971), 45–48. DOI: 10.4153/CMB-1971-007-1.
- A. Bonato, P. Gordinowicz and P. Prałat, *Bounds and constructions for n-e.c. tournaments*, Contributions to Discrete Mathematics **5**(2) (2010), published 2010-09-28. DOI: 10.55016/ojs/cdm.v5i2.62061.
- N. Y. Javier, B. Llano and R. Zuazua, *2- and 3-existentially closed tournaments*, Contributions to Discrete Mathematics **21**(1) (2026), published 2026-02-27. DOI: 10.55016/0sre1423.
- *Erdős problem #902 — working report*, accessible at https://www.erdosproblemaday.com/report/902, dated 2026-07-28. Its order-67 deletion-critical computation concerns the common-dominator property.
