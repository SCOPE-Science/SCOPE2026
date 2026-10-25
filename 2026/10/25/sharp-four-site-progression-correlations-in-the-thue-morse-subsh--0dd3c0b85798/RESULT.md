# Sharp four-site progression correlations in the Thue–Morse subshift

## Finding

Let \(t_j=(-1)^{s_2(j)}\) be the balanced Thue–Morse sequence, where \(s_2(j)\) is the sum of the binary digits of a nonnegative integer \(j\). On its uniquely ergodic two-sided subshift, let \(\mu\) be the invariant probability measure, and put
\[
C(h)=\int x_0x_hx_{2h}x_{3h}\,d\mu(x),\qquad h\in\mathbb Z_{\ge1}.
\]
Then
\[
\boxed{|C(h)|\le\tfrac13\quad\text{for every }h\ge1,\qquad
|C(h)|=\tfrac13\iff h\text{ is a power of }2.}
\]
Every equality case has positive sign: \(C(2^k)=1/3\) for all integers \(k\ge0\). In particular, the maximal absolute fourth-order correlation of four distinct equally spaced Thue–Morse observations is exactly \(1/3\), attained only at dyadic spacings.

## Assumptions and scope

All offsets are nonnegative integers, all spacings are strictly positive integers, and all expectations are with respect to the uniquely invariant measure of the balanced Thue–Morse substitution \(+\mapsto+-\), \(-\mapsto-+\). The correlation is an infinite-volume cylinder expectation, equivalently the limit of natural-density averages of \(t_jt_{j+h}t_{j+2h}t_{j+3h}\). The statement neither concerns arbitrary four-point index sets nor general substitutions.

For integers \(a,b,c\ge0\), define
\[
\eta(a,b,c)=\int x_0x_ax_bx_c\,d\mu(x).
\]
Repeated offsets are permitted in the auxiliary function, but the four offsets in the final claim are distinct.

## Proof

**1. Renormalization.** Since \(t_{2j}=t_j\) and \(t_{2j+1}=-t_j\), conditioning on even or odd starting indices gives, with \(q_i=\lfloor m_i/2\rfloor\) and \(e_i=m_i-2q_i\),
\[
\eta(m_1,m_2,m_3)=\frac{(-1)^{e_1+e_2+e_3}}2
\bigl(\eta(q_1,q_2,q_3)+\eta(q_1+e_1,q_2+e_2,q_3+e_3)\bigr).
\tag{1}
\]
Unique ergodicity guarantees the limits, and the parity decomposition is valid for them. This established fourth-order renormalization is also stated by Ong and follows from the general even-order formula of Baake–Coons [2, 3].

**2. Eight closed offset states.** In the fixed order
\[
\mathcal S=((0,0,0),(0,0,1),(0,1,1),(0,1,2),
(1,1,1),(1,1,2),(1,2,2),(1,2,3)),
\]
write \(V_i(h)=\eta(h+a_i,2h+b_i,3h+c_i)\), where \((a_i,b_i,c_i)\) is state \(i\), indexed from zero. For \(h=2k+r\) with \(r\in\{0,1\}\), use \(L=(r+a_i,2r+b_i,3r+c_i)\), \(q=\lfloor L/2\rfloor\) coordinatewise, and \(e=L-2q\). Applying (1) yields the exact eight-state relation
\[
V_i(2k+r)=\frac{(-1)^{e_1+e_2+e_3}}2
\bigl(V_{\operatorname{idx}(q)}(k)+V_{\operatorname{idx}(q+e)}(k)\bigr).
\tag{2}
\]
Both indexed triples belong to \(\mathcal S\). Thus \(V(2k)=M_0V(k)\) and \(V(2k+1)=M_1V(k)\), where every matrix row is a signed average of two coordinates. To remove any ambiguity, the following is the complete exact transition certificate; each entry \((\varepsilon,u,v)\) specifies the row \(\varepsilon(V_u+V_v)/2\):

| State | \(M_0\) row | \(M_1\) row |
|---|---|---|
| 0 | \((+,0,0)\) | \((+,2,5)\) |
| 1 | \((-,0,1)\) | \((-,3,5)\) |
| 2 | \((+,0,2)\) | \((+,3,6)\) |
| 3 | \((-,1,2)\) | \((-,3,7)\) |
| 4 | \((-,0,4)\) | \((-,5,6)\) |
| 5 | \((+,1,4)\) | \((+,5,7)\) |
| 6 | \((-,2,4)\) | \((-,6,7)\) |
| 7 | \((+,2,5)\) | \((+,7,7)\) |

**3. Initial values.** The pair correlation \(\int x_0x_1\,d\mu=-1/3\) follows by decomposing its average into parity classes: \(\eta_2(1)=-(1+\eta_2(1))/2\). Also \(\eta_2(2)=\eta_2(1)=-1/3\). Splitting \(C(1)\) into even and odd starting positions gives
\[
C(1)=\tfrac12\bigl(1+\eta_2(2)\bigr)=\tfrac13.
\]
Collapsing repeated offsets consequently gives
\[
V(0)=(1,-\tfrac13,1,-\tfrac13,-\tfrac13,-\tfrac13,-\tfrac13,\tfrac13),
\]
and (2) supplies the independent base vector
\[
V(1)=M_1V(0)=\tfrac13(1,1,-1,0,1,0,0,1).
\tag{3}
\]
In particular, every coordinate of \(V(1)\) lies in \([-1/3,1/3]\).

**4. Uniform sharp bound.** For \(h\ge2\), \(\lfloor h/2\rfloor\) is a positive integer smaller than \(h\). Equation (2) and the fact that signed means preserve the interval \([-1/3,1/3]\) prove inductively that every coordinate of \(V(h)\) lies in this interval. The desired correlation is \(C(h)=V_0(h)\).

**5. Exhaustive equality rigidity.** For any vector whose coordinates lie in \([-1/3,1/3]\), encode a coordinate by `+` when it equals \(1/3\), by `-` when it equals \(-1/3\), and by `.` when its absolute value is strictly less than \(1/3\). A signed average of two coordinates saturates \(\pm1/3\) if and only if *both inputs are saturated with the same sign*. Consequently (2) induces an exact deterministic action on saturation strings, without inspecting nonsaturated numerical values.

Starting with the string `++-.+..+` from (3), the full reachable transition table, with \(0\) meaning \(h\mapsto2h\) and \(1\) meaning \(h\mapsto2h+1\), is

| Saturation string | \(0\) successor | \(1\) successor |
|---|---|---|
| `++-.+..+` | `+-..-+..` | `.......+` |
| `+-..-+..` | `+....-..` | `........` |
| `+....-..` | `+.......` | `........` |
| `+.......` | `+.......` | `........` |
| `.......+` | `........` | `.......+` |
| `........` | `........` | `........` |

This table is exhaustive: its six rows contain the initial state and are closed under both transitions. It is checked by applying the eight exact signed-average rows in Step 2. Its first coordinate is saturated only along the path consisting exclusively of \(0\)-transitions from the initial state: every \(1\)-transition leads to `.......+` or `........`, neither of which can ever recover saturation in its first coordinate. Reading the binary expansion of a positive integer from its leading \(1\) constructs precisely the transitions from \(h=1\). Therefore \(|V_0(h)|=1/3\) precisely if the binary expansion of \(h\) has no further \(1\), equivalently \(h=2^k\). All first-coordinate saturations in the table carry the plus sign, proving the equality value \(1/3\). This completes the proof.

## Verification

The standalone `verify.py` uses only the Python standard library. Running `python verify.py` checks, with exact rational arithmetic, the eight states, both signed-average matrices, both base vectors, closure and the complete six-type saturation-transition table, and all \(10{,}000\) smallest positive lag evaluations. It separately computes \(35\) literal long-block sums of the Thue–Morse signs as numerical cross-checks. The unrestricted theorem follows from the induction and six-state closure in the proof; finite lag calculations alone would not establish it.

Expected output begins `VERIFY_OK: eight exact renormalization rows, six exhaustive saturation types, 10000 exact lag evaluations, 35 independent block comparisons`.

## Relationship to prior work

The Thue–Morse subshift, its strict ergodicity and conventional two-point autocorrelations are classical; [1] is a motivating pre-2016 study. Baake and Coons [2, Proposition 4.1 and Corollary 4.5] give the broader arbitrary-order correlation recursion and explain that all correlations can be recursively calculated from corner data. Ong [3, Proposition 2.6] already gives the four-point recursion and exhibits graphical arrays of four-site correlations. These *general recursions and computational frameworks are not new*. The evaluated statement here is narrower but different: a global **optimal absolute bound for the four-term arithmetic-progression slice** and a complete classification of all integer spacings attaining it, proved using an explicit saturation automaton. The cited general formulas permit computations at each specified spacing; they do not in their inspected sections state the unrestricted sharp maximum and dyadic equality classification. No claim of independently certified historical priority is made.

## Limitations

The conclusion applies only to four equally spaced distinct times in the balanced binary Thue–Morse system. It does not bound arbitrary four-site correlations by \(1/3\) (those with coincident sites may equal \(1\)), classify non-equally-spaced quadruples, or determine the full range or minimum of \(C(h)\). It uses classical higher-correlation recurrence technology; an earlier unlocated explicit extremal specialization is possible. The proof and verifier have not received independent audit.

## References

[1] M. Baake, F. Gähler, U. Grimm, “Spectral and topological properties of a family of generalised Thue–Morse sequences,” arXiv:1201.1423 (first posted 2012-01-06), https://arxiv.org/html/1201.1423v2. Section 2, Thue–Morse dynamics and correlations.

[2] M. Baake and M. Coons, “Correlations of the Thue–Morse sequence,” arXiv:2209.07102 (2022), https://arxiv.org/html/2209.07102v2. Section 4, in particular Proposition 4.1 and Corollary 4.5.

[3] D. C. Ong, “Abstract art generated by Thue–Morse correlation functions,” arXiv:2209.11162 (2022), https://arxiv.org/html/2209.11162v1. Sections 2.3 and 3, especially Proposition 2.6.
