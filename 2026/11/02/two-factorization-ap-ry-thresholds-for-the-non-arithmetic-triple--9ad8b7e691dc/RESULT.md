# Two-factorization Apéry thresholds for the non-arithmetic triple \(\langle m,m+1,m+3\rangle\)

## Finding
For every integer \(m\ge4\), the least integer in each residue class modulo \(m\) admitting two distinct nonnegative coin representations with denominations \(m\), \(m+1\), \(m+3\) is given by an explicit two-piece formula. More precisely, write
\[
d_m(N)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^3:\;mx+(m+1)y+(m+3)z=N\},
\quad f(t)=\lfloor t/3\rfloor+(t\bmod3),
\]
where \(t\bmod3\) is the remainder in \(\{0,1,2\}\). Define, for \(0\le r<m\),
\[
H_m(r)=\begin{cases}1+f(m+r),&0\le r\le2,\\2+f(r),&3\le r<m.\end{cases}
\]
Then, for all \(q\ge0\) and \(0\le r<m\),
\[
\boxed{d_m(qm+r)\le1\iff q<H_m(r).}
\]
Equivalently, the complete first two-factorization threshold set (the \(1\)-Apéry set) is
\[\boxed{\{mH_m(r)+r:0\le r<m\}.}\]
The largest integer with at most one representation is
\[
\boxed{F_1(m)=\begin{cases}13,&m=4,\\(\lfloor m/3\rfloor+3)m-1-\mathbf1_{m\equiv1\pmod3},&m\ge5.\end{cases}}
\]
The number of **positive** integers with at most one representation is
\[
\boxed{G_1^{+}(m)=\sum_{r=0}^{m-1}f(r)+3m-4.}
\]
If the zero integer is counted as a \(1\)-gap, as in the standard \(p\)-genus convention, the count is \(G_1^{+}(m)+1\). Writing \(m=3h+a\), with \(a\in\{0,1,2\}\), the displayed positive count equals \((3h^2+21h-8)/2\), \((3h^2+23h-2)/2\), or \((3h^2+25h+6)/2\), respectively.

## Assumptions and scope
The parameter \(m\) is any integer at least four. Each ordered triple of nonnegative coefficients is a distinct representation; reordering coins is not an extra representation. The digit remainder is always the canonical nonnegative remainder. The theorem classifies the threshold for **at least two** representations; it does not classify thresholds for three or more representations. All quantifiers include every residue and every nonnegative quotient, with no asymptotic restriction on \(m\).

## Proof
Fix \(m\ge4\), \(0\le r<m\), and \(N=qm+r\), where \(q\ge0\). Every solution of the representation equation satisfies
\[
N=m(x+y+z)+y+3z.
\]
Write \(j=q-(x+y+z)\). Because \(y+3z=N-m(x+y+z)\ge0\), this is a nonnegative integer, and
\[
 y+3z=r+jm,\qquad x+y+z=q-j.
\]
Conversely, for any \(j\ge0\), writing \(t=r+jm\), every choice of \(z\in\{0,1,\dots,\lfloor t/3\rfloor\}\) gives \(y=t-3z\), and a representation exactly when \(t-2z\le q-j\); the remaining coefficient is \(x=q-j-(t-2z)\ge0\). Such representations with different \(j\), or different \(z\) at fixed \(j\), are distinct.

For each \(t\ge0\), the possible values of \(y+z=t-2z\) are
\[
 f(t),\ f(t)+2,\dots, f(t)+2\lfloor t/3\rfloor.
\]
Thus the \(j=0\) class supplies one representation as soon as \(q\ge f(r)\) and, when \(r\ge3\), supplies a second precisely when \(q\ge f(r)+2\). For \(r\le2\), the \(j=0\) class has at most one representation for all \(q\).

Any representation with \(j\ge1\) requires \(q\ge j+f(r+jm)\). We claim that this is minimized at \(j=1\). Indeed, for every nonnegative \(t\), \(f(t+m)\ge f(t)\) when \(m\ge4\). This follows by writing \(t=3v+u\), \(m=3h+a\), with \(u,a\in\{0,1,2\}\), and checking the nine possible pairs of remainders. Hence \(j+f(r+jm)\) increases strictly with \(j\). The first \(j\ge1\) representation therefore appears precisely at \(q=1+f(r+m)\).

If \(r\le2\), this first \(j=1\) representation is distinct from the existing \(j=0\) representation and is the second overall, so its quotient is \(H_m(r)=1+f(r+m)\). If \(r\ge3\), the comparison \(f(r+m)\ge f(r)+1\) holds for all \(m\ge5\), by the same nine-remainder check. When \(m=4\), necessarily \(r=3\), and directly \(f(7)=3\ge f(3)+1=2\). Thus no \(j\ge1\) representation precedes \(q=f(r)+2\); the second \(j=0\) representation appears exactly there. This establishes \(H_m(r)=f(r)+2\) and proves the biconditional for every \(q\), because adding one \(m\)-coin injects all representations of \(qm+r\) into those of \((q+1)m+r\).

The largest integer with at most one representation is
\[
 F_1(m)=\max_{0\le r<m}\bigl((H_m(r)-1)m+r\bigr).
\]
Inspecting the three residue classes of \(m\) modulo three shows that, for \(m\ge5\), the maximizing residue is \(m-1\) when \(m\equiv0,2\pmod3\), and \(m-2\) when \(m\equiv1\pmod3\). The latter class has \(m\ge7\). These give the stated formula. At \(m=4\) the four threshold quotients are \((3,4,3,3)\), and the maximum is \(13\).

The count of nonnegative integers with at most one representation is \(\sum_rH_m(r)\), because exactly \(H_m(r)\) quotients are excluded for each residue. Directly substituting the two-piece formula yields
\[
\sum_{r=0}^{m-1}H_m(r)=\sum_{r=0}^{m-1}f(r)+3m-3.
\]
There is one excluded zero, which has exactly one representation. Subtracting it gives the positive count. Finally \(\sum_{r=0}^{3h+a-1}f(r)=3h(h+1)/2+ah+\mathbf1_{a=2}\), giving the displayed quasipolynomial in \(m\). \(\square\)

## Verification
The included standalone `verify.py` implements an exact integer dynamic program for the unrestricted three-coin denumerant, then checks every threshold in every residue for all \(4\le m\le150\) (\(147\) distinct parameter values, \(11319\) residue thresholds). It verifies both boundary quotients, the full closed-form maximum and genus formulas, and small explicit instances independently of the algebraic proof. Run with `python3 verify.py` using standard Python; no external files or dependencies are required. Finite checks do not establish the infinite theorem: that is the function of the preceding proof.

## Relationship to prior work
Komatsu and Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions* (arXiv:2206.13052; initially public 2022-06-27), developed \(p\)-Apéry sets and explicit formulas for the family \(\langle a,a+d,a+2d\rangle\). The present triple \(\langle m,m+1,m+3\rangle\) is not an arithmetic progression, and the published arithmetic-progression formulas do not directly imply its second-representation threshold set. Their general \(p\)-Apéry framework and the maximum/sum method are acknowledged prior machinery, not a new definition or deduction. Komatsu and Ying, *\(p\)-numerical semigroups with \(p\)-symmetric properties* (arXiv:2207.08962), investigates general properties but does not state this specific two-factorization classification in the material inspected. O'Neill and Pelayo, *Apéry Sets of Shifted Numerical Monoids* (arXiv:1708.09527), determine ordinary Apéry sets of shifted families under suitable size hypotheses; their cited main theorem is about the first representable value rather than the first value with **two** representations. The classification here uses the second-smallest coin-factorization length and the one-wrap competition, not merely ordinary membership. Generic algorithms for fixed-dimensional generalized Frobenius numbers remain applicable but do not themselves supply these explicit all-parameter formulas.

## Limitations
Only the threshold for two representations is classified. The sources searched and source passages inspected do not exclude implicit earlier derivations or an equivalent specialization in other denumerant work. No independent scientific audit has been carried out.

## References
1. T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first submitted 2022-06-27), https://arxiv.org/abs/2206.13052.
2. T. Komatsu and H. Ying, *\(p\)-numerical semigroups with \(p\)-symmetric properties*, arXiv:2207.08962 (2022), https://arxiv.org/abs/2207.08962.
3. C. O'Neill and R. Pelayo, *Apéry Sets of Shifted Numerical Monoids*, arXiv:1708.09527 (2017; later revised), https://arxiv.org/abs/1708.09527.
4. D. Mohammed, *Generalised Frobenius numbers: geometry of upper bounds* (2017 thesis), https://orca.cardiff.ac.uk/id/eprint/98161/1/Final%20Thesis.pdf.
