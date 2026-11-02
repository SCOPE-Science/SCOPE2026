# Nonlinearity exactly determines quadratic annihilators of odd five-variable feedback forms

## Finding

Consider any Boolean function on five binary variables of the form
\[
f(x_0,y)=x_0\oplus g(y),\qquad y\in\mathbb F_2^4,
\]
where the truth table of \(g\) has odd Hamming weight. Define \(\mathrm{NL}(h)\) to be the minimum Hamming distance from \(h\) to an affine Boolean function. For \(b\in\mathbb F_2\), let
\[
\mathcal A_{2,b}(f)=\{p\in\mathrm{RM}(2,5):p(x)\,(f(x)\oplus b)=0\text{ for every }x\in\mathbb F_2^5\}.
\]
Here \(\mathrm{RM}(2,5)\) denotes all Boolean polynomials of algebraic degree at most two, and multiplication is pointwise over \(\mathbb F_2\). The exact identities are
\[
\boxed{\dim\mathcal A_{2,0}(f)=\dim\mathcal A_{2,1}(f)=5-\mathrm{NL}(g)=5-\tfrac12\mathrm{NL}(f).}
\]
The only possible nonlinearity values are \(\mathrm{NL}(f)\in\{2,6,10\}\), with corresponding dimensions \(4,2,0\). Consequently the algebraic immunity, defined as the minimum degree of a nonzero annihilator of \(f\) or \(1\oplus f\), satisfies
\[
\boxed{\mathrm{AI}(f)=3\quad\Longleftrightarrow\quad\mathrm{NL}(f)=10,}
\]
with \(\mathrm{AI}(f)=2\) in the other two cases. Thus maximum five-variable nonlinearity within this odd-feedback family is equivalent to optimal five-variable algebraic immunity, and the complete dimensions of both quadratic-annihilator spaces are fixed by the nonlinearity.

**Maximum-period corollary.** A binary five-stage nonlinear feedback shift register generating one cycle through all \(32\) states necessarily has the above odd-feedback form. Among its \(2{,}048\) distinct feedback functions, precisely \(896\) have algebraic immunity three; the other \(1{,}152\) have immunity two. More precisely, the three pairs \((\mathrm{NL}(f),\dim\mathcal A_{2,b}(f))\) occur with multiplicities \((2,4):24\), \((6,2):1128\), and \((10,0):896\). These **nonlinearity multiplicities themselves were already published** by Sönmez Turan (2012, Table 2); the deduction of the algebraic-immunity and quadratic-annihilator classification is the additional content here.

## Assumptions and scope

All functions are Boolean functions over \(\mathbb F_2\), all polynomial operations are taken modulo \(u^2=u\), and all ranks and dimensions are over \(\mathbb F_2\). The condition \(\operatorname{wt}(g)\equiv1\pmod2\) is essential: it is not imposed on arbitrary balanced five-variable Boolean functions. It is satisfied by every one-cycle five-stage feedback rule; the unrestricted theorem covers all \(32{,}768\) odd-weight truth tables \(g\), whether or not the feedback has maximum period. Inputs are ordered \((x_0,y_1,y_2,y_3,y_4)\); for the cycle test the successor of integer state \(x\) is obtained by dropping its least significant bit and inserting \(f(x)\) at the most significant position.

## Proof

**1. Three affine-distance cases.** The coefficient of the degree-four monomial in the algebraic normal form of \(g\) is the parity of its truth-table weight. The odd-weight assumption therefore gives \(\deg g=4\). Every affine function has even truth-table weight on four variables, so every affine distance from \(g\) is odd. The Walsh–Parseval identity implies that a four-variable Boolean function has nonlinearity at most six. Thus \(s=\mathrm{NL}(g)\) is exactly one of \(1,3,5\). Choose an affine \(\ell\) attaining this distance and set \(g\oplus\ell=1_S\), the indicator of a set \(S\subseteq\mathbb F_2^4\) of size \(s\).

For \(s=1\) or \(3\), the points of \(S\) are affinely independent. For \(s=5\), they also must be affinely independent: otherwise the five points lie in an affine hyperplane \(H\), whose indicator \(1_H\) is affine on four variables; then \(g\oplus(\ell\oplus1_H)=1_{H\setminus S}\) has weight three, contrary to \(s=5\). An invertible affine transformation of \(y\) can therefore put \(S\) into one of the three normal forms
\[
\{0\},\qquad \{0,e_1,e_2\},\qquad \{0,e_1,e_2,e_3,e_4\}.
\]
Replacing \(g(y)\) by \(g(Ay+b)\oplus\ell(y)\) is induced on \(f\) by an invertible affine change of its five input variables (including \(x_0\mapsto x_0\oplus\ell(y)\)). Such changes preserve nonlinearity, algebraic immunity, and the dimensions of annihilator spaces of every fixed degree. It thus suffices to compute for these normal forms.

**2. Exact quadratic restriction rank.** Every \(p\in\mathrm{RM}(2,5)\) has a unique expression
\[
p(x_0,y)=A(y)\oplus x_0 B(y),\quad A\in\mathrm{RM}(2,4),\quad B\in\mathrm{RM}(1,4).
\]
The dimensions are \(11\) and \(5\), hence \(\dim\mathrm{RM}(2,5)=16\). On the graph \(x_0=g(y)\), its restriction is \(A(y)\oplus g(y)B(y)\). Consequently the restriction map has rank \(11+\operatorname{rank}T_g\), where \(T_g\) sends the five coefficients of the affine \(B\) to the coefficients of the five degree-three-or-four monomials in \(gB\). Using the row order \(y_1y_2y_3,y_1y_2y_4,y_1y_3y_4,y_2y_3y_4,y_1y_2y_3y_4\), and column order \(1,y_1,y_2,y_3,y_4\), the five binary row strings for the three normal forms are respectively

| \(S\) | Five rows of \(T_g\), in the stated order | Rank |
|---|---|---:|
| \(\{0\}\) | `10000`, `10000`, `10000`, `10000`, `10000` | 1 |
| \(\{0,e_1,e_2\}\) | `11100`, `11100`, `01000`, `00100`, `11100` | 3 |
| \(\{0,e_1,e_2,e_3,e_4\}\) | `01110`, `01101`, `01011`, `00111`, `11111` | 5 |

Each entry follows by a four-variable Möbius transform of \(1_S B\). Ordinary binary row elimination gives the displayed ranks \(s\). Hence the restriction kernel on \(x_0=g(y)\) has dimension \(16-(11+s)=5-s\). On the other graph \(x_0=g(y)\oplus1\), the restriction is \(A\oplus gB\oplus B\), and \(B\in\mathrm{RM}(2,4)\) does not change the quotient rank. These two kernels are precisely the respective spaces \(\mathcal A_{2,b}(f)\) (with their labels exchanged if one swaps graphs). Therefore both dimensions are \(5-s\).

**3. Algebraic immunity and nonlinearity.** There is no nonzero degree-one annihilator: its graph restriction would give \(A(y)\oplus c g(y)=0\) with \(A\) affine and \(c\in\mathbb F_2\), impossible since \(g\) has degree four. Thus \(\mathrm{AI}(f)\ge2\). If \(s=1\) or \(3\), the positive quadratic kernel gives immunity two. If \(s=5\), both quadratic kernels vanish. But \(\dim\mathrm{RM}(3,5)=26>16\), so restriction to either 16-point graph admits a nonzero polynomial of degree at most three. Immunity is then exactly three.

For every affine Boolean function on five variables, the coefficient of \(x_0\) is either one or zero. In the first case its distance from \(f\) is twice the distance from \(g\) to an affine function of \(y\). In the second case each \(y\)-pair contributes exactly one disagreement, giving distance \(16\). Since \(s\le5\), this proves \(\mathrm{NL}(f)=2s\), finishing both identities.

**4. Maximal-period specialization.** A one-cycle five-stage feedback rule must be nonsingular, hence must have the form \(x_0\oplus g(y)\). Its cycle-count parity forces \(g\) to have odd truth-table weight, as recalled in Sönmez Turan's 2012 Section 3. Table 2 of that paper already determines its exact nonlinearity distribution at order five: \(24\) at two, \(1128\) at six, and \(896\) at ten. Applying the proved theorem to these existing counts gives the exact algebraic-immunity split and quadratic-annihilator dimensions. A separate complete traversal of the 65,536 feedback tables reproduces the 2,048 one-cycle cases and the same joint distribution.

## Verification

Run `python3 verify_nl_ai.py` using the attached standard-library-only checker. It independently (i) computes the three five-row matrices by Möbius transform, (ii) enumerates all 32,768 odd-weight four-variable Boolean truth tables, (iii) determines their nonlinearity by direct affine-distance comparison, and (iv) computes the rank of degree-two polynomial evaluations on both five-variable graphs using a separate 16-column evaluation matrix. The joint counts for \((\mathrm{NL}(g),\dim\mathcal A_{2,b})\) are \((1,4):512\), \((3,2):17920\), \((5,0):14336\). It independently enumerates all one-cycle feedbacks and obtains \((\mathrm{NL}(f),\dim\mathcal A_{2,b})\) counts \((2,4):24\), \((6,2):1128\), and \((10,0):896\). The program exits only after all exact assertions pass and prints `VERIFY_OK`. Exhaustive finite checks corroborate, but do not replace, the all-functions proof above.

## Relationship to prior work

Sönmez Turan's 2012 *On the Nonlinearity of Maximum-length NFSR Feedbacks* establishes the necessary parity condition, the relation between feedback nonlinearity and the reduced Boolean function, and **the complete order-five nonlinearity multiplicities**. Those published results are inputs, not novelty claims. Çalık, Sönmez Turan and Özbudak (2010) study structural properties and monomial restrictions of maximum-length feedback functions. Carlet, Dalai, Gupta and Maitra (2006) develop algebraic immunity, general nonlinearity implications, and annihilator counts, but the inspected material does not give this exact odd-feedback quadratic-restriction rank law. Boyar, Find and Peralta (2016) discuss the broader non-equivalence of various nonlinearities; the equality here is special to the stated family. The 2020 studies by Zhou–Hu–Guan and Kuznetsov and collaborators also address de Bruijn or maximum-length feedback nonlinearity; accessible summaries do not mention this algebraic-immunity rank law, but not all full texts could be inspected. The exact coupling of both degree-two annihilator dimensions to nonlinearity and its derived maximum-period algebraic-immunity split are the claims made here, subject to further historical-priority review.

## Limitations

The unrestricted theorem requires exactly five input variables and the **odd-weight four-variable feedback component**. It is not asserted for even-weight components, arbitrary balanced five-variable functions, or longer registers. Algebraic immunity by itself does not certify resistance to all algebraic or fast algebraic attacks. The 2012 nonlinearity distribution is not presented as new. Historical priority could be affected by an unindexed earlier specialized classification, and no independent mathematical audit has been performed.

## References

1. Meltem Sönmez Turan, *On The Nonlinearity of Maximum-length NFSR Feedbacks*, Cryptology ePrint Archive 2012/112 (first archival receipt February 29, 2012), https://eprint.iacr.org/2012/112 ; lawful author-hosted PDF: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=910672 (particularly Sections 3–4 and Table 2).
2. Çağdaş Çalık, Meltem Sönmez Turan, Ferruh Özbudak, *On Feedback Functions of Maximum Length Nonlinear Feedback Shift Registers*, IEICE Transactions on Fundamentals E93-A(6), 1226–1231 (2010), https://doi.org/10.1587/transfun.E93.A.1226 ; open manuscript https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=905987.
3. Claude Carlet, Deepak Kumar Dalai, Kishan Chand Gupta, Subhamoy Maitra, *Algebraic Immunity for Cryptographically Significant Boolean Functions: Analysis and Construction*, IEEE Transactions on Information Theory 52(7), 3105–3121 (2006), https://doi.org/10.1109/TIT.2006.876253.
4. Joan Boyar, Magnus G. Find, René Peralta, *On Various Nonlinearity Measures for Boolean Functions*, Cryptography and Communications 8, 371–394 (2016), https://doi.org/10.1007/s12095-015-0150-9.
5. Congwei Zhou, Bin Hu and Jie Guan, *On the Maximum Nonlinearity of De Bruijn Sequence Feedback Function*, ePrint 2020/835, https://eprint.iacr.org/2020/835 (indexed excerpts and abstract were accessible, but the complete PDF was not retrieved).
6. Alexandr Kuznetsov et al., *Combining and Filtering Functions in the Framework of Nonlinear-Feedback Shift Register*, International Journal of Computing 19(2), 247–256 (2020), https://doi.org/10.47839/ijc.19.2.1768 (abstract-level comparison).
