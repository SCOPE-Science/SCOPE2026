# An exact quintic for the \(k=3\) hardcore-SOS critical coupling
## Finding
For the three-state hardcore-SOS \(p=\infty\) model on the Cayley tree of order \(k=3\), let \(\widehat\theta_c\approx0.4812\) be the second critical coupling identified by Jahnel and Rozikov, and put \(z=\widehat\theta_c^2\). Then \(z\) is exactly the unique real root in \(23/100<z<6/25\) of
\[
2187z^5-2916z^4+1940z^3-660z^2+96z-4=0.
\]
Consequently
\[
\widehat\theta_c=0.48123282404100283873007266995368838\ldots.
\]
For that root,
\[
\eta=-\frac{6044868z^4-6966324z^3+4037567z^2-1053986z+68606}{5814},\qquad w=z(\eta-1),
\]
and \(\eta>24/5\), \(w>1/2\). These values satisfy exactly the upper-branch tangency system in Remark 1 of the source. The new statement is the exact algebraic characterization of the critical coupling, not the source's phase-count theorem.

## Assumptions and scope
The model, normalization, and variables are those of Jahnel--Rozikov, arXiv:2404.03297v1. The state space is \(\{0,1,2\}\), the interaction is the hardcore-SOS model at \(p=\infty\), and the Cayley tree has order \(k=3\). The source reduces the nontrivial translation-invariant boundary-law problem to a reciprocal equation and, after setting \(\eta=x+x^{-1}\), introduces
\[
a(w)=w^2+3w+\frac1w,\qquad b(\eta)=\frac{\eta^3+7}{(\eta-1)(\eta+2)}.
\]
Its upper branch is determined by \(a(w)=b(\eta)\) with \(w>1/2\). Remark 1 characterizes the second critical point by tangency together with \(w=(\eta-1)\theta^2\). No assertion is made here about other interactions, other tree orders, or nontranslation-invariant Gibbs measures.

## Proof
Write \(z=\theta^2\). At the source's critical upper-branch tangency,
\[
a(w)=b(\eta),\qquad \frac{b'(\eta)}{a'(w)}=z,\qquad w=z(\eta-1).
\]
Since
\[
a'(w)=2w+3-\frac1{w^2},\qquad
b'(\eta)=\frac{(\eta+1)^2(\eta^2-7)}{(\eta-1)^2(\eta+2)^2},
\]
the derivative equation is equivalently
\[
(\eta-1)b'(\eta)=w a'(w).
\]
Clear denominators in the two equations \(a(w)=b(\eta)\) and \((\eta-1)b'(\eta)=w a'(w)\), substitute \(w=z(\eta-1)\), and eliminate \(\eta\). The eliminant factors as
\[
z^7(2z-1)^6(8z-3)H(z),
\]
where
\[
H(z)=2187z^5-2916z^4+1940z^3-660z^2+96z-4.
\]
The source's value \(\widehat\theta_c\approx0.4812\) places \(z\) in \((23/100,6/25)\). The factors \(z\), \(2z-1\), and \(8z-3\) do not vanish on that interval, so the physical critical point must satisfy \(H(z)=0\).

An exact Sturm sequence gives exactly one real zero of \(H\) in \((23/100,6/25)\), with \(H(23/100)>0\) and \(H(6/25)<0\). Reducing the eliminated system modulo \(H\) yields the reconstruction
\[
\eta=-\frac{6044868z^4-6966324z^3+4037567z^2-1053986z+68606}{5814},\qquad w=z(\eta-1).
\]
Exact Sturm checks on the same isolating interval show \(\eta>24/5\) and \(w>1/2\). Substitution of these rational functions into both the branch equation and the tangency equation gives numerators divisible by \(H\); hence the unique isolated root reconstructs an upper-branch tangency. This identifies it with the source's second critical point.

## Verification
The bundled `verify.py` uses exact rational polynomial arithmetic. It verifies the endpoint signs, a Sturm root count of one for \(H\) on \((23/100,6/25)\), the exact reconstruction identities modulo \(H\), and the strict inequalities \(\eta>24/5\) and \(w>1/2\) throughout the isolating interval. It then computes a high-precision decimal by bisection only after the exact checks. A clean replay prints a line beginning `VERIFY_OK roots=1` and gives
\[
z=0.23158503093447879974986012215799116\ldots,
\qquad
\widehat\theta_c=0.48123282404100283873007266995368838\ldots.
\]
The decimal computation is not used as proof of uniqueness or of the algebraic identities.

## Relationship to prior work
Jahnel and Rozikov derive the \(k=3\) reciprocal equation, reduce it to the \((\eta,w)\) formulation above, prove the phase-count result, and report the second critical value numerically as approximately \(0.4812\). Their Remark 1 explicitly states that finding the exact value requires solving the displayed upper-branch tangency system. The present calculation solves that exact-value step by an isolating quintic and a rational reconstruction of the tangency variables. The related paper arXiv:2402.09839 treats the binary Cayley tree, so it does not imply the \(k=3\) algebraic threshold here.

## Limitations
The quintic characterization concerns only the second critical coupling \(\widehat\theta_c\) in the source's \(k=3\), \(p=\infty\) translation-invariant analysis. It does not provide a radical expression, does not re-prove the complete Gibbs-measure classification, and does not address extremality or nontranslation-invariant measures. An equivalent algebraic elimination could exist in weakly indexed notes not located in the literature checks.

## References
B. Jahnel and U. Rozikov, “Gibbs measures for hardcore-SOS models on Cayley trees,” arXiv:2404.03297v1 (2024), later J. Stat. Mech. (2024), DOI 10.1088/1742-5468/ad5433.

B. Jahnel and U. Rozikov, “Three-state \(p\)-SOS models on binary Cayley trees,” arXiv:2402.09839v1 (2024).
