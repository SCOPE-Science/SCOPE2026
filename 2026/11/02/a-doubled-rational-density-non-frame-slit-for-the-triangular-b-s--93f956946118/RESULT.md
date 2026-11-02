# A doubled rational-density non-frame slit for the triangular B-spline

## Finding
Let \(Q_2(x)=(1-|x|)_+\), and use the usual Gabor lattice \(\mathcal G(Q_2,a,b)=\{e^{2\pi i mbx}Q_2(x-na):m,n\in\mathbb Z\}\). For every real \(b\) with \(11/4\le b\le13/4\), put \(a=3/(4b)\), so \(ab=3/4\). **This Gabor system is not a frame for \(L^2(\mathbb R)\).** In fact, its continuous \(3\times4\) Zibulski–Zeevi matrix has rank at most two at the same fiber \((x,t)=(0,0)\) throughout the full interval. Its rank there is exactly two except at \(b=3\), where the rank is one.

The interval extends the general 2016 non-frame range \(23/8\le b\le25/8\) at density \(3/4\) to the strictly larger interval \(11/4\le b\le13/4\). No assertion is made about frame behavior outside the claimed interval or about global maximality of the interval.

## Assumptions and scope
Both lattice parameters are positive, \(b\in[11/4,13/4]\), \(a=3/(4b)\), and the window is the normalized symmetric order-two cardinal B-spline \(Q_2(x)=\max(1-|x|,0)\). This window is continuous, compactly supported and belongs to the Feichtinger algebra \(M^1(\mathbb R)\). At rational density \(ab=p/q=3/4\), the rank criterion applies to the continuous \(p\times q\) fiber matrices. There is no assumption of generic sampling, and endpoints are included.

## Proof
The following form of the Zibulski–Zeevi matrix is given in Ghosh–Selvan, equation (2.4):
\[
\Theta_{k\ell}(x,t)=\sum_{n\in\mathbb Z}Q_2(x+aqn+a\ell+k/b)e^{-2\pi i aqnt},
\quad 0\le k<3,\quad0\le\ell<4.
\]
Their Theorem 2.2 says a frame requires rank three at every fiber. At \((x,t)=(0,0)\), since \(aq=3/b\) and \(a\ell=3\ell/(4b)\),
\[
\Theta_{k\ell}(0,0)=\frac1b\sum_{n\in\mathbb Z}(b-|k+3\ell/4+3n|)_+.
\]
Define the \(3\)-periodic function \(F_b(s)=b^{-1}\sum_{n\in\mathbb Z}(b-|s+3n|)_+\). Fix any \(s\in[1/4,11/4]\). If \(11/4\le b\le13/4\), then the only positive summands of \(bF_b(s)\) are those at distances \(s\) and \(3-s\). Indeed, \(s,3-s\le11/4\le b\), while the next distances \(3+s\) and \(6-s\) are at least \(13/4\ge b\); all more distant translates are larger. Thus
\[
F_b(s)=\frac{(b-s)+(b-(3-s))}{b}=2-\frac3b=:c(b).
\]
Reduce the eight arguments \(k+3\ell/4\), for \(k=1,2\) and \(\ell=0,1,2,3\), modulo three. They are respectively
\[
(1,7/4,5/2,1/4),\qquad(2,11/4,1/2,5/4),
\]
all in \([1/4,11/4]\). Hence rows one and two (zero-indexed) are **exactly equal**, both \((c,c,c,c)\). For row zero, the arguments for \(\ell=1,2,3\) also lie in \([1/4,11/4]\), whereas its \(\ell=0\) argument is zero. At zero, the positive contributions occur at distances zero and (if \(b>3\)) twice distance three, giving
\[
 c_0(b):=F_b(0)=\begin{cases}1,&11/4\le b\le3,\\3-6/b,&3\le b\le13/4.\end{cases}
\]
Consequently the **entire exact fiber** equals
\[
\Theta(0,0)=\begin{pmatrix}
 c_0&c&c&c\\c&c&c&c\\c&c&c&c
\end{pmatrix},\quad c=2-3/b,\quad c_0-c=|b-3|/b.
\]
The nonzero vector \((0,1,-1)\) belongs to its left kernel for every allowed \(b\), so rank is at most two. Since \(c>0\), the rank is exactly two for \(b\ne3\) and one for \(b=3\). The fiber is continuous because \(Q_2\in M^1\), so a deficient rank at one fiber precludes a positive uniform lower Gabor frame bound by the quoted rank criterion. This proves the claim, including both endpoints.

## Verification
The standalone `checker.py` uses exact rational arithmetic and an explicit finite periodization over translates (all distant terms are zero). It reconstructs the full \(3\times4\) fiber and tests the closed formula and rank at 406 rational values in the stated interval; it additionally checks loss of the specific row equality at two points outside it. These finite tests verify the computation but are not a proof for all real \(b\): that is furnished by the distance inequalities above. Reproduce with `python checker.py` using Python's standard library.

## Relationship to prior work
Lemvig–Nielsen (2015/2016), Theorem 7, proves non-frame behavior for rational \(ab=p/q\) whenever \(|b-\operatorname{round}(b)|\le1/(2q)\) for \(Q_2\). At \(p/q=3/4\), this covers exactly \([23/8,25/8]\); its Remark 3 explicitly says that general interval may be nonoptimal, distinguishing full rank from its zero-row sufficient mechanism. Their Theorem 8 proves a different, larger interval at density \(5/6\), not \(3/4\). Gröchenig's 2015 partition-of-unity obstruction is a discrete-point result requiring a denominator factorization not available for \(q=4\). Ghosh–Selvan (first public 2023-10-02) proves other second-order B-spline non-frame conjectures; its parameter families have odd numerator over an even denominator of special form or half-integer \(b\), and do not imply this \(3/4\) interval. Lemvig's 2026 hyperbolic family requires \(q=r\mu\) with \(r\ge2\), \(\mu\ge3\), so it does not cover \(q=4\). The present explicit equal-row mechanism more than doubles the \(b\)-interval length known from the general 2016 theorem in this specific rational-density case. This is a statement-level comparison, not a claim of exhaustive historical priority.

## Limitations
Only the claimed sufficient non-frame interval is established; whether all or part of the adjacent hyperbola outside it is framed remains unknown here. The calculation uses the triangular spline exactly, not arbitrary compactly supported windows or higher-order splines. Historical-priority risk remains for unlocated sources, unpublished notes and any broader theorem not encountered. No independent mathematical validation has been performed.

## References
- R. Ghosh and A. A. Selvan, *Obstructions for Gabor frames of the second order B-spline*, arXiv:2310.01141, first submitted 2023-10-02, especially §§1–2 and Theorem 2.2.
- J. Lemvig and K. H. Nielsen, *Counterexamples to the B-spline conjecture for Gabor frames*, arXiv:1507.03982, originally submitted 2015-07-14, especially Theorems 7–8 and Remark 3.
- K. Gröchenig, *Partitions of unity and new obstructions for Gabor frames*, arXiv:1507.08432 (2015), Proposition 2.
- J. Lemvig, *A new family of hyperbolic slits in the Gabor frame set of B-spline generators*, arXiv:2601.07642 (2026), Theorems 1.2–1.3.
- K. H. Nielsen, *The Frame Set of Gabor Systems with B-spline Generators*, Technical University of Denmark thesis (2015), §5.
