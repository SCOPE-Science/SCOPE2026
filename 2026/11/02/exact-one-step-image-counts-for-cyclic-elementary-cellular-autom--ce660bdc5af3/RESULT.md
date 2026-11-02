# Exact one-step image counts for cyclic elementary cellular automaton Rule 110

## Finding
For each integer \(n\geq1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) apply elementary cellular automaton Rule 110 simultaneously with indices taken modulo \(n\), and set \(a_n=|\operatorname{Im}F_n|\), with the formal convention \(a_0=1\). Then
\[
\sum_{n\geq0}a_nz^n=
\frac{1-3z+4z^2-2z^3-2z^4+7z^5-10z^6+8z^7-2z^8+z^{10}}
{(1-z)(1-z-z^4)(1-2z+z^2-z^3-z^4)}.
\]
In particular, for \(n=1,\ldots,15\), the exact numbers of distinct outputs are
\[
1,2,5,10,22,41,79,154,302,582,1113,2125,4058,7737,14725.
\]
There is a unique positive dominant root \(\lambda\approx1.897179401065396\) of \(t^4-2t^3+t^2-t-1\), and
\[
a_n=\lambda^n+O(1.381^n).
\]
Thus the proportion of all \(n\)-bit circular states reachable in one update is asymptotic to \((\lambda/2)^n\). This concerns **one-step** reachability; it does not classify eventual image sets or long-term attractors.

## Assumptions and scope
Rule 110 is the binary radius-one local map \(f:\{0,1\}^3\to\{0,1\}\) with
\[
(f(0,0,0),f(0,0,1),f(0,1,0),f(0,1,1),f(1,0,0),f(1,0,1),f(1,1,0),f(1,1,1))=(0,1,1,1,0,1,1,0).
\]
Precisely, \((F_n(x))_i=f(x_{i-1},x_i,x_{i+1})\), with all subscripts interpreted modulo \(n\). The \(n=1,2\) cases use the same convention, so some neighbor indices coincide. Strings are rooted and labeled by their \(n\) positions: rotations of an output count as different unless the bit strings are actually identical. The generating-function variable is formal, and all counts are exact integers.

## Proof
**1. Closed-walk recognition.** Index the ordered binary pair states as \(00,01,10,11\). For each output bit \(c\), put an edge from pair \((a,b)\) to pair \((b,d)\) whenever \(f(a,b,d)=c\). Let \(M_c\) be the corresponding Boolean \(4\times4\) adjacency matrix. With row-major bit indexing \(4i+j\) and least significant bit first, the 16-bit matrix encodings are \(M_0=33025\) and \(M_1=17090\). A circular output word \(y_0\cdots y_{n-1}\) has a circular preimage if and only if the Boolean product \(M_{y_0}\cdots M_{y_{n-1}}\) has a nonzero diagonal entry: its closed walk consists of the consecutive overlapping input pairs. The criterion also holds for rings of length one and two.

**2. Finite complete recognition algebra.** Begin with the identity Boolean matrix \(I\), and close under right multiplication by \(M_0\) and \(M_1\), with Boolean \(\lor,\land\) arithmetic. The exhaustive exact closure has 75 distinct matrices. Exactly 61 have some diagonal entry equal to one. Enumerate these matrices by breadth-first discovery starting with \(I\), processing output bits in order \(0,1\); the included verifier defines this order and recomputes the entire closure with integer bit operations. Write \(T\) for the \(75\times75\) nonnegative integer transition matrix, counting both possible output letters separately, and \(v\) for its 0–1 column vector marking the 61 accepting matrices. If \(e_I\) is the initial row vector, then
\[
a_n=e_I T^n v\qquad(n\geq0).
\]
This equality counts **distinct outputs**, not their numbers of input preimages, because every output word follows exactly one deterministic path in the relation automaton.

**3. Exact finite recurrence certificate.** Let
\[
p(t)=t^9-4t^8+6t^7-5t^6+t^5+4t^4-4t^3+2t^2-1.
\]
Direct integer evaluation of the 75 components of the vector \(T^2p(T)v\), as implemented in `verify.py`, gives the zero vector. Every matrix, edge and component is regenerated from the eight local truth-table entries; there are no external numeric tables. Multiplication on the left by \(e_IT^k\) for any \(k\geq0\) therefore proves for every \(n\geq11\)
\[
a_n-4a_{n-1}+6a_{n-2}-5a_{n-3}+a_{n-4}+4a_{n-5}-4a_{n-6}+2a_{n-7}-a_{n-9}=0.
\]
The exact initial values \(a_0,\ldots,a_{10}\) are \(1,1,2,5,10,22,41,79,154,302,582\), also regenerated from \(T\). At \(n=10\) the recurrence left side is instead 1. Put
\[
D(z)=(1-z)(1-z-z^4)(1-2z+z^2-z^3-z^4)
\]
and expand it as \(1-4z+6z^2-5z^3+z^4+4z^5-4z^6+2z^7-z^9\). The recurrence makes \(D(z)\sum a_nz^n\) a polynomial of degree at most ten; exact multiplication by the 11 initial terms gives precisely the stated numerator. This establishes the rational identity for **every** ring length, rather than merely extrapolating a finite census.

**4. Root formula and growth.** A direct rational-polynomial identity gives
\[
\sum_{n\geq0}a_nz^n=\frac1{1-z}-z-
 z\frac{B'(z)}{B(z)}+z\frac{C'(z)}{C(z)},
\quad B(z)=1-2z+z^2-z^3-z^4,\quad C(z)=1-z-z^4.
\]
If \(\rho\) ranges over the four roots of \(t^4-2t^3+t^2-t-1\) and \(\sigma\) ranges over those of \(t^4-t^3-1\), both with multiplicities, the formal logarithmic derivative proves the exact identity
\[
a_n=1+\sum_{\rho}\rho^n-\sum_{\sigma}\sigma^n-\mathbf1_{\{n=1\}}\qquad(n\geq0).
\]
For the first quartic, the unique positive root exceeding one is \(\lambda\in(1.897,1.898)\); the unique negative root is \(-b\), where \(b\in(0.483,0.485)\). The other two roots are a conjugate pair, each of modulus \(1/\sqrt{\lambda b}<1.05\) by the product of all roots. Existence and uniqueness of these real roots follow by the sign and monotonicity of \(t^2(t-1)^2-t-1\) on \(t\geq1\) and of \(b^4+2b^3+b^2+b-1\) on \(b>0\), together with the absence of positive roots in \([0,1]\). The polynomial \(t^4-t^3-1\) has a unique positive real root \(\mu\in(1.380,1.381)\) by Descartes' rule of signs and monotonicity beyond one; every complex root satisfies \(|\sigma|^4\leq|\sigma|^3+1\), hence \(|\sigma|\leq\mu\). Therefore all contributions other than \(\lambda^n\) are \(O(1.381^n)\). The coefficient of the dominant term is exactly one.

## Verification
Run `python3 verify.py` using only the Python standard library. It recomputes the Boolean de Bruijn matrices, enumerates all 75 relation states, constructs the 61 accepting states, verifies all 75 exact integer identities in \(T^2p(T)v=0\), checks the rational numerator and denominator and root power-sum formula, and independently enumerates all binary input words to compare their distinct one-step outputs for every \(1\leq n\leq16\). The verifier prints `VERIFY_OK` upon success. The direct finite enumeration is corroborative; the all-length proof is the exact 75-component identity and its mathematical implication.

## Relationship to prior work
Rule 110's local map and its universality are classical. Earlier work on its de Bruijn/subset diagrams establishes preimage recognition and Garden-of-Eden tests (Seck Tuoh Mora, Martínez and McIntosh; Martínez et al.). In particular, the 2007 open-access manuscript treats languages of Rule-110 glider phases and finite forbidden patterns rather than an all-length count of *distinct cyclic one-step outputs*. Published example calculations of finite cyclic preimages likewise do not give the identity above as an inspected statement. The present count applies the established recognition method to the **distinct-output enumeration** problem and proves a specific rational generating function and sharp growth rate. It is not a claim that the de Bruijn method or Rule 110 is new. The full text of one relevant specialized preimage paper was not available for inspection; historical priority is not independently certified.

## Limitations
The theorem is restricted to binary Rule 110 on finite periodic rings after exactly one synchronous update. No fixed-density refinement, multi-step image, computational-complexity improvement, or general classification of all elementary rules is asserted. A relevant earlier full text was not obtained; exact historical priority remains a risk even though the comparisons available did not reveal this formula. This is a self-review, not independent certification.

## References
1. G. J. Martínez et al., *Determining a regular language by glider-based structures called phases fi1 in Rule 110*, arXiv:0706.3348v1, first submitted 22 June 2007. https://arxiv.org/abs/0706.3348
2. J. C. Seck Tuoh Mora, G. J. Martínez and H. V. McIntosh, *Calculating Ancestors in One-dimensional Cellular Automata*, https://doi.org/10.1142/S0129183104006625. Earlier preimage and subset-diagram methodology.
3. *Cellular Automata / Counting Preimages*, Wikibooks, https://en.wikibooks.org/wiki/Cellular_Automata/Counting_Preimages. Explanation of cyclic de Bruijn diagonal preimage criterion.
4. *Cellular Automata / Examples on Rule 110*, Wikibooks, https://en.wikibooks.org/wiki/Cellular_Automata/Examples_on_Rule_110. Explicit prior local matrices and forbidden-pattern examples.
5. E. W. Weisstein, *Rule 110*, MathWorld, https://mathworld.wolfram.com/Rule110.html. Historical setting and local rule.
