# Exact right-special factors in irrational three-rotor coincidence codes

## Finding
For every irrational real slope \(\sigma>1\), start the ultra-high-energy (free straight-line) three-rotor coincidence coding at the grid origin with trajectory \((x(t),y(t))=(t,\sigma t)\), \(t\geq0\). The symbol \(0\) records the initial triple coincidence; afterward \(1\) records crossings of horizontal grid lines, \(3\) crossings of vertical grid lines, and \(2\) is inserted immediately before each ordinary crossing. Write its one-sided infinite code, indexed from zero, as
\[
X=X_0X_1X_2\cdots=0\,2\,b_0\,2\,b_1\,2\,b_2\cdots,\qquad b_j\in\{1,3\}.
\]
For every integer \(n\geq1\), **the unique right-special factor of length \(n\) in the entire one-sided word \(X\) is exactly**
\[
\boxed{R_n=X_nX_{n-1}\cdots X_1.}
\]
Its distinct right continuations are precisely \(R_n1\) and \(R_n3\). Every other length-\(n\) factor has exactly one right continuation. Thus this establishes the reverse-initial-prefix conjecture posed in Section 5.3.1 of Krishnaswami and Rameshan (2026), uniformly over every irrational \(\sigma>1\) and every length \(n\).

The right-special word is explicit from the slope. If \(\alpha=1/(1+\sigma)\), then
\[
b_j=1+2\bigl(\lfloor(j+2)\alpha\rfloor-\lfloor(j+1)\alpha\rfloor\bigr),
\quad j=0,1,2,\ldots .
\]
In particular, its letters can be computed by finitely many floor evaluations without searching the infinite language.

## Assumptions and scope
The statement concerns the **exact free straight-line, or ultra-high-energy limit** of the physical model, not finite energy. The irrational condition excludes any subsequent simultaneous horizontal/vertical crossing. All factors are finite contiguous subwords at indices \(j\geq0\) of the one-sided word \(X\); a factor \(w\) is right-special precisely when both \(w1\) and \(w3\) occur as such subwords (equivalently, at least two distinct one-letter right extensions occur). The index-zero \(0\) occurs only once, at the beginning. The integer \(n\) is arbitrary and positive; no restriction on its size or on continued-fraction coefficients of \(\sigma\) is imposed.

## Proof
**1. The correct characteristic intercept comes from crossing times.** Rescale the straight-line trajectory so the grid has unit spacing. Horizontal crossings occur at \(x=h/\sigma\), for integers \(h\geq1\), and vertical crossings at \(x=q\), for integers \(q\geq1\). Irrationality makes these strictly ordered. Before the vertical event \(x=q\), exactly \(\lfloor q\sigma\rfloor\) horizontal events and \(q-1\) other vertical events have occurred. Therefore that event has zero-based index
\[
j=\lfloor q\sigma\rfloor+q-1
=\left\lfloor\frac{q}{\alpha}\right\rfloor-1,
\qquad\alpha=\frac1{1+\sigma}\in(0,1/2).
\]
Equivalently, a vertical event occurs at event index \(j\) exactly when the open interval \(((j+1)\alpha,(j+2)\alpha)\) contains an integer, so that
\[
c_j:=\frac{b_j-1}{2}
=\lfloor(j+2)\alpha\rfloor-\lfloor(j+1)\alpha\rfloor.
\]
Thus \(c\) is the characteristic mechanical coding with **phase \(\alpha\)**, rather than a generic Sturmian word with arbitrary phase. The index shift is essential to the claimed reversed prefix.

**2. All characteristic prefixes are left-special.** Define for any phase \(\theta\) and integer \(j\) the rotational code
\[
s^{(\theta)}_j=\lfloor\theta+(j+1)\alpha\rfloor-\lfloor\theta+j\alpha\rfloor.
\]
Then \(c_j=s^{(\alpha)}_j\) for every \(j\geq0\). Fix any \(m\geq1\). Because \(\alpha\) is irrational, the finite list \(s^{(\theta)}_0,\ldots,s^{(\theta)}_{m-1}\) is locally constant near \(\theta=\alpha\). But the immediately preceding symbol is
\[
s^{(\theta)}_{-1}=\lfloor\theta\rfloor-\lfloor\theta-\alpha\rfloor,
\]
which equals \(1\) immediately **below** \(\theta=\alpha\) and \(0\) immediately **above** it. Both finite extended blocks occur in \(c\), because the irrational rotation by \(\alpha\) has a dense forward orbit and these patterns persist on nonempty open phase intervals. Hence every length-\(m\) prefix of \(c\) has both possible left predecessors.

**3. Reversal transfers left-special to right-special.** The language of the rotation coding is closed under reversal. Indeed, away from endpoints, the coding interval \([1-\alpha,1)\) and its complement are preserved by the circle reflection \(\rho(\theta)=1-\alpha-\theta\pmod1\), and \(\rho(\theta+\alpha)=\rho(\theta)-\alpha\). Reflecting the forward segment of any generic rotation orbit therefore reverses its finite label word. Density extends this conclusion to the full Sturmian factor language. Thus the reversal of each length-\(m\) prefix of \(c\) is right-special. The coding is Sturmian, with \(m+1\) factors of length \(m\). Since each binary factor has at least one right continuation, this complexity difference forces **exactly one** right-special factor of each positive length \(m\). For the empty word (\(m=0\)), both letters are possible successors. Replacing binary digits \(0,1\) with rotor symbols \(1,3\) preserves these assertions for \(b\).

**4. Lift through the alternating \(2\)-markers.** Any rotor factor containing the initial \(0\) occurs once and has one right continuation. Any rotor factor ending in \(1\) or \(3\) must be followed by \(2\), hence cannot be right-special. Therefore every right-special factor ends in \(2\). For even length \(n=2m\), \(m\geq1\), such a factor has the shape
\[
b_i\,2\,b_{i+1}\,2\cdots b_{i+m-1}\,2;
\]
for odd length \(n=2m+1\), \(m\geq1\), it has the shape
\[
2\,b_i\,2\,b_{i+1}\,2\cdots b_{i+m-1}\,2.
\]
Its two possible right extensions are exactly the two extensions of the underlying length-\(m\) base word. Step 3 identifies the unique branching base factor as \(b_{m-1}\cdots b_0\), giving in both parities precisely the reverse \(X_n\cdots X_1\). The remaining case \(n=1\) is \(R_1=2\), which is followed by both \(1\) and \(3\). All other factors have only one extension. This proves all quantifiers and the claimed uniqueness. \(\square\)

## Verification
The standalone, standard-library-only `verify.py` independently merges horizontal/vertical crossings by the exact integer test \(h^2<d v^2\) for the seven irrational slopes \(\sigma=\sqrt d\), \(d\in\{2,3,5,6,7,10,11\}\). It checks this event code against the algebraic floor coding for the first 3,200 events in each case. On 12,000 base symbols for each slope it checks all factor complexities and right-extension sets for lengths \(1\leq n\leq80\). On replay, the program prints `VERIFY_OK` with 24,080 finite assertions. These tests are checks of coding and indexing only; the unrestricted result follows from the proof above.

## Relationship to prior work
Krishnaswami and Rameshan, arXiv:2606.25766v1, Section 5.3.4, establish the Sturmian/rotor-marker correspondence and the complexity formula \(p_X(n)=n+3\). Their Section 5.3.1 and Discussion explicitly leave the **identity of the right-special factor** as a conjecture/open question, checking only small lengths for sample slopes. The characteristic-word and reversal properties of Sturmian languages are classical; in particular the characteristic-word characterization is recorded by Bucci, De Luca and Zamboni, arXiv:1205.5946v1, Proposition 2.3. Here those known ingredients are used without claiming them as new. The rotor-specific point is to recover the **correct shifted phase from the origin-crossing indexing**, and then pass the reversed characteristic prefix through the one-sided four-symbol code, including its exceptional initial \(0\) and parity-dependent marker positions. Searches identified no prior proof of this precise conjecture; earlier equivalent derivations cannot be excluded.

## Limitations
No conclusion is claimed for finite-energy rotor orbits, rational slopes, trajectories launched away from the grid origin, or the author's separate conjectures about chaotic trajectories. The statement is not a new general Sturmian-word theorem: it is a rigorous identification of the unique branching factors in the physically defined nonbinary coding. The finite verification program is not an infinite proof. Priority beyond the inspected open-access literature remains subject to independent specialist review.

## References
1. G. S. Krishnaswami and A. Rameshan, *Symbol sequences from three-rotor coincidences and their word-complexity*, arXiv:2606.25766v1 (June 24, 2026), Sections 5.1 and 5.3.1–5.3.4 and Discussion. https://arxiv.org/html/2606.25766v1
2. M. Bucci, A. De Luca and L. Q. Zamboni, *Some characterizations of Sturmian words in terms of the lexicographic order*, arXiv:1205.5946v1 (2012), Section 2.3, Proposition 2.3. https://arxiv.org/html/1205.5946v1
3. M. Morse and G. A. Hedlund, *Symbolic Dynamics II: Sturmian Trajectories*, American Journal of Mathematics 62 (1940), 1–42 (classical background).
