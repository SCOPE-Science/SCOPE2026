# Sharp positivity boundary and conservative splitting for an SEIRSD discretization

## Finding
For the sequential normalized SEIRSD NSFD formula (7)–(8) in [1], all five compartments remain nonnegative for **every** admissible initial state and every positive denominator step if and only if the immunity-loss rate satisfies \(\alpha=0\). For \(\alpha>0\), the printed update may return a **negative deceased fraction in one step**, even from strictly positive susceptible, exposed, infected, and recovered fractions. This is not a roundoff phenomenon: the defect has an exact algebraic description and persists for every positive step size after suitable strictly positive initial data are selected.

Its sharp one-step feasibility condition, with \(i^+\) denoting the printed updated infected fraction, is
\[
\boxed{\quad (1+\alpha h)d+h\bigl[\mu(1+\alpha h)+\alpha\gamma h\bigr]i^+\geq\alpha^2 h^2 r.\quad}
\tag{1}
\]
Equality is permitted. Failure of (1) means \(d^+<0\). A separate, explicit **transfer-balanced** sequential discretization is given below; it conserves total population, preserves the full simplex for every positive step and every \(\alpha\geq0\), is first-order consistent, and is identical to the original map in the permanent-immunity case \(\alpha=0\).

## Assumptions and scope
Write \((s,e,i,r,d)\) for normalized susceptible, exposed, infectious, recovered, and deceased fractions. The state domain is
\[
\Delta_* =\{(s,e,i,r,d)\in[0,1]^5:s+e+i+r+d=1,\quad 1-d>0\}.
\]
The parameters obey \(\beta,\sigma,\gamma,\mu>0\), \(\alpha\geq0\), and \(h>0\). The source uses \(h=\varphi(k)\), with \(\varphi(k)>0\) and \(\varphi(k)=k+O(k^2)\) as \(k\downarrow0\). For a current state in \(\Delta_*\), set \(q=\beta i/(1-d)\). Superscript \(+\) denotes the next iterate. The **exact printed map** is
\[
\begin{aligned}
s^+&=\frac{s+\alpha h r}{1+hq}, &
e^+&=\frac{e+hq s^+}{1+\sigma h},\\
i^+&=\frac{i+\sigma h e^+}{1+(\gamma+\mu)h}, &
r^+&=\frac{r+\gamma h i^+}{1+\alpha h},\\
d^+&=1-s^+-e^+-i^+-r^+ .
\end{aligned}
\tag{2}
\]
All denominators are positive. The claim concerns the **five-coordinate map (2)** as printed, not a postprocessed simulation with manually clipped deaths. Source [1] explicitly sets \(\alpha=0\) in its reported numerical experiments; those experiments are not challenged by this result.

## Proof
**Step 1: exact mortality balance.** Rearranging the first four equations in (2) gives
\[
\begin{aligned}
s^+-s &=h(-qs^++\alpha r),\\
e^+-e &=h(qs^+-\sigma e^+),\\
i^+-i &=h(\sigma e^+-(\gamma+\mu)i^+),\\
r^+-r &=h(\gamma i^+-\alpha r^+).
\end{aligned}
\]
Sum these four equalities and use the definition of \(d^+\) to obtain the **exact identity**
\[
d^+-d=h\mu i^++\alpha h(r^+-r).
\tag{3}
\]
From the fourth equality, \(r^+-r=h(\gamma i^+-\alpha r)/(1+\alpha h)\). Substituting in (3) yields
\[
\boxed{\;d^+-d=h\mu i^++\frac{\alpha h^2}{1+\alpha h}(\gamma i^+-\alpha r).\;}
\tag{4}
\]
Multiplication by \(1+\alpha h>0\) gives (1). Thus (1) is **necessary and sufficient**, not an estimate. The nonnegative mortality-flux condition \(d^+\geq d\) has the independent exact criterion
\[
[\mu(1+\alpha h)+\alpha\gamma h]i^+\geq\alpha^2 h r.
\tag{5}
\]
In particular, conservation by defining a residual \(d^+\) does not itself ensure nonnegativity or monotone deaths.

**Step 2: sharp universal positivity boundary.** In (2), the updated \(s^+,e^+,i^+,r^+\) are nonnegative for every state in \(\Delta_*\). If \(\alpha=0\), (4) becomes \(d^+=d+h\mu i^+\geq0\); hence (2) maps \(\Delta_*\) into itself. Its living fraction remains positive for all finite steps because at least one of \(s^+,e^+,i^+,r^+\) is strictly positive whenever the original living population is positive.

Conversely fix **arbitrarily** \(\alpha>0\), \(h>0\), and positive \(\beta,\sigma,\gamma,\mu\). Choose any \(r\in(0,1)\), set \(d=0\), \(e=i=\varepsilon>0\), and \(s=1-r-2\varepsilon>0\). As \(\varepsilon\downarrow0\), the explicit expressions in (2) give \(i^+\to0\), continuously. The numerator of (1), when interpreted as \((1+\alpha h)d^+\), tends to the **strictly negative** value \(-\alpha^2h^2r\). It is therefore negative for every sufficiently small positive \(\varepsilon\). This proves failure of universal simplex preservation for every \(\alpha>0\) and every positive step. By continuity, after slightly increasing \(d\) above zero and adjusting \(s\) to retain unit total, examples exist in the strict interior \(s,e,i,r,d>0\) as well. Together these arguments prove the if-and-only-if classification.

**Step 3: exact rational witness.** Take
\[
\begin{gathered}
h=\alpha=\beta=\sigma=1,\qquad\gamma=\mu=\frac1{10},\\
(s,e,i,r,d)=\left(\frac14,\frac1{100},\frac1{100},\frac{73}{100},0\right).
\end{gathered}
\]
Formula (2) then gives
\[
(s^+,e^+,i^+,r^+,d^+)=
\left(\frac{98}{101},\frac{199}{20200},\frac{401}{24240},\frac{177353}{484800},-\frac{58583}{161600}\right).
\tag{6}
\]
Every initial living fraction is strictly positive. All rational identities and their unit sum were checked independently with the bundled standard-library program `verifier.py`.

**Step 4: a sequential positive and conservative replacement.** Keep the same \(q=\beta i/(1-d)\) and positive \(h\). Make a first, exactly matched, recovered-to-susceptible transfer:
\[
w=\frac{\alpha h r}{1+\alpha h},\qquad \bar s=s+w,\qquad\bar r=r-w=\frac r{1+\alpha h}.
\]
Then define
\[
\begin{aligned}
\widetilde s^+&=\frac{\bar s}{1+hq},&
\widetilde e^+&=\frac{e+hq\widetilde s^+}{1+\sigma h},\\
\widetilde i^+&=\frac{i+\sigma h\widetilde e^+}{1+(\gamma+\mu)h},&
\widetilde r^+&=\bar r+\gamma h\widetilde i^+,\\
\widetilde d^+&=d+\mu h\widetilde i^+.
\end{aligned}
\tag{7}
\]
Each quantity is nonnegative; the first transfer has \(0\leq w\leq r\). For the remaining four flows, write \(T=hq\widetilde s^+\), \(P=\sigma h\widetilde e^+\), \(G=\gamma h\widetilde i^+\), \(M=\mu h\widetilde i^+\). Their changes are
\[
\widetilde s^+-\bar s=-T,\quad
\widetilde e^+-e=T-P,\quad
\widetilde i^+-i=P-G-M,\quad
\widetilde r^+-\bar r=G,\quad
\widetilde d^+-d=M.
\]
These sum to zero exactly, while \(\bar s+\bar r=s+r\); therefore the full normalized total stays equal to one and deaths never decrease. A nonzero living population stays nonzero after any finite step. With \(h=\varphi(k)=k+O(k^2)\), direct expansion of (7) about \(k=0\) gives the right-hand side of the continuous SEIRSD model [1, Eq. (4)] with local defect \(O(k^2)\), hence first-order consistency for smooth solutions. Finally, if \(\alpha=0\), then \(w=0\), \(\bar s=s\), \(\bar r=r\), and (7) agrees exactly with all five updates in (2), including \(d^+=d+h\mu i^+\) from (4).

For the same rational input used in (6), (7) yields
\[
(\widetilde s^+,\widetilde e^+,\widetilde i^+,\widetilde r^+,\widetilde d^+)=
\left(\frac{123}{202},\frac{13}{1616},\frac{243}{16160},\frac{59227}{161600},\frac{243}{161600}\right),
\]
which is in the probability simplex exactly.

## Verification
Run `python3 verifier.py` with Python 3. The program uses exact `fractions.Fraction` arithmetic to reproduce (6), the exact mortality-balance identity, the sharp frontier for the stated witness, and the conservative replacement's rational output. It also checks the \(\alpha=0\) coincidence on representative rational inputs. Expected final output: `VERIFY_OK`. The program's finite checks support the arithmetic only; the statements for all steps and all admissible states follow from the symbolic proof above.

## Relationship to prior work
The target paper [1] prints the nonnegative-update formulas and says that its full scheme stays in the invariant simplex, but its susceptible inflow evaluates immunity waning at \(r\) while recovered outflow uses \(r^+\). The resulting unmatched flux appears exactly in (3). This finding determines the **sharp** parameter boundary of that specific five-compartment map and gives a rigorously positive sequential replacement.

The earlier four-compartment SIRSD paper [2, Sec. 5, Eqs. (9)–(10)] already writes a related unmatched-flow mortality term and juxtaposes two different time-level treatments of recovery. This related structure is explicitly recognized; the identity behind (3) and the general idea of matching compartmental transfers are **not** claimed as new in isolation. The later gain–loss neural-ODE paper [3, Sec. 4] outlines standard pairwise-flux and Patankar conservation principles but does not analyze map (2), its exact feasibility boundary, or its sequential five-compartment replacement. A distinct SEIARD NSFD discretization [4, Eqs. (15)–(16)] pairs each loss and gain and updates mortality by explicit nonnegative death transfers. The new statement is local to [1]'s **particular printed five-coordinate recurrence**, not a new general positivity theory.

## Limitations
This is a result about the formal discrete map as written in arXiv:2606.15201v1. It neither disputes the well-posedness of the continuous ODE nor establishes instability or error bounds for the learned forecasting algorithm. The source's reported numerical experiments set \(\alpha=0\), precisely the case where the obstruction vanishes; there is no basis here to call their reported simulated trajectories negative. The corrected map (7) is proved first-order consistent and feasible, not higher-order accurate, asymptotically stable for all parameters, or statistically superior. General conservative gain–loss splitting is established prior art; only the stated sharp boundary, specific mathematical witness, and implementation for the printed SEIRSD map are at issue. A later revision of [1] could alter the formulas, and absolute literature priority cannot be established from searches alone.

## References
[1] A. Zinihi, M. Ehrhardt, and M. R. Sidi Ammi, *A Koopman-PINN Framework for Epidemic Models: Parameter Inference and Forecasting*, arXiv:2606.15201v1, first publicly dated 13 June 2026; §2 and §4.1, Eqs. (7)–(8). https://arxiv.org/html/2606.15201v1

[2] A. Zinihi, M. Ehrhardt, and M. R. Sidi Ammi, *A Koopman Operator Framework for Nonlinear Epidemic Dynamics: Application to an SIRSD Model*, arXiv:2508.16766v1, 22 August 2025; §5, Eqs. (9)–(10). https://imacm.uni-wuppertal.de/fileadmin/imacm/preprints/2025/imacm_25_13.pdf

[3] A. Zinihi, M. Ehrhardt, and M. R. Sidi Ammi, *Structure-Preserving Neural ODEs via Nonstandard Finite Difference Discretization*, arXiv:2607.10858v1, 12 July 2026; §§3–4. https://arxiv.org/pdf/2607.10858

[4] A. Zinihi, M. Ehrhardt, and M. R. Sidi Ammi, *Actuarial Analysis of an Infectious Disease Insurance Based on an SEIARD Epidemiological Model*, 2026, §4, Eqs. (15)–(16), DOI:10.1080/10920277.2026.2664588. https://www.tandfonline.com/doi/full/10.1080/10920277.2026.2664588
