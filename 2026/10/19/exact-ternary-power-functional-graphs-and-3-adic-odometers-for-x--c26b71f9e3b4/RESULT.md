# Exact ternary-power functional graphs and 3-adic odometers for \(x\mapsto x+x^2\)

## Finding
Let \(F(x)=x+x^2\). On \(\mathbb Z_3\), its only periodic point is \(0\). For each integer \(t\ge1\), precisely \(2\cdot3^{t-1}\) balls of radius \(3^{-2t}\), indexed by residues \(a\pmod{3^{2t}}\) with \(v_3(a)=t\), are minimal invariant components:
\[
B_{t,a}=a+3^{2t}\mathbb Z_3.
\]
Each restriction \(F|_{B_{t,a}}\) is conjugate to the adding machine on \(\mathbb Z_3\). All other points enter \(3\mathbb Z_3\) after one or two steps, with the possible exceptional destination \(0\).

For each integer \(n\ge1\), let \(F_n\) act on \(R_n=\mathbb Z/3^n\mathbb Z\). Its periodic vertices are exactly \(3R_n\); a nonzero vertex of truncated valuation \(1\le t<n\) has exact period
\[
T_n(x)=3^{\max\{n-2t,0\}}.
\]
The number of fixed vertices is \(3^{\lfloor n/2\rfloor}\); for every \(1\le t\le\lfloor(n-1)/2\rfloor\), there are exactly \(2\cdot3^{t-1}\) distinct cycles of length \(3^{n-2t}\). Hence
\[
\zeta_n(z)=(1-z)^{-3^{\lfloor n/2\rfloor}}\prod_{t=1}^{\lfloor(n-1)/2\rfloor}(1-z^{3^{n-2t}})^{-2\cdot3^{t-1}}.
\]
For \(n\ge3\), the maximum period is \(3^{n-2}\), attained by exactly \(2\cdot3^{n-2}\) vertices, a constant proportion \(2/9\).

Every periodic vertex has one unique depth-one predecessor in \(2+3R_n\). There are no other depth-one vertices, and every vertex in \(1+3R_n\) has depth exactly two. For each depth-one vertex \(u\), let \(q_n(u)\) be the number of incoming depth-two leaves. Among the \(3^{n-1}\) depth-one vertices, exactly one has \(q_n=3^{\lfloor n/2\rfloor}\); for every \(1\le r\le\lfloor(n-1)/2\rfloor\), exactly \(3^{n-2r-1}\) have \(q_n=2\cdot3^r\); every remaining depth-one vertex has \(q_n=0\). These formulas completely determine the directed functional graph for every \(n\).

## Assumptions and scope
The same integer polynomial \(F(x)=x(1+x)\) is considered both on the ring of ternary integers \(\mathbb Z_3\) and on its reductions \(R_n\), for every positive integer \(n\). A depth is the least number of forward iterates needed to reach a periodic vertex. The valuation \(v_3(x)\) for a nonzero ternary integer is its exponent of \(3\), and for a nonzero finite residue is the exponent of \(3\) in any integer representative, truncated at \(n\). For the zero residue, use truncated valuation \(n\). The zeta function is the usual Artin–Mazur formal series \(\exp(\sum_{k\ge1}\#\operatorname{Fix}(F_n^k)z^k/k)\). The entire claim is an exact statement in these specified rings, not a generalization to other primes.

## Proof
**1. Residue routing and invertibility.** Modulo \(3\), the map is \(0\mapsto0\), \(2\mapsto0\), \(1\mapsto2\). On \(3\mathbb Z_3\), \(F(x)=x(1+x)\) preserves the exact valuation of every nonzero point. Also \(F'(x)=1+2x\equiv1\pmod3\). An induction by base-three digit lifting (or Hensel's lemma) gives a bijection of \(3\mathbb Z_3\) and of every finite \(3R_n\). Likewise \(F'(x)\equiv2\pmod3\) on \(2+3\mathbb Z_3\), and \(F\) maps this residue class bijectively onto \(3\mathbb Z_3\); the corresponding map \(2+3R_n\to3R_n\) is also bijective. The residue routing proves the asserted depths once all points of \(3R_n\) are shown periodic.

**2. Critical displacement lemma.** If \(x\in3\mathbb Z_3\setminus\{0\}\), write \(t=v_3(x)\ge1\). For every \(k\ge0\),
\[
v_3(F^{3^k}(x)-x)=2t+k.\tag{1}
\]
At \(k=0\), the displacement is \(x^2\). Suppose (1) holds and set \(G=F^{3^k}\), \(u=G(x)-x\), \(s=v_3(u)=2t+k\ge2\). Because every forward iterate of \(x\) remains in \(3\mathbb Z_3\), \(a=G'(x)\equiv1\pmod3\). Integral polynomial Taylor expansion, applied three times, yields
\[
G^3(x)-x=u(1+a+a^2)+u^2w,\qquad w\in\mathbb Z_3.
\]
Writing \(a=1+3b\) gives \(1+a+a^2=3(1+3b+3b^2)\), of exact valuation one. The first summand therefore has valuation \(s+1\), while the second has valuation at least \(2s>s+1\). This proves (1) by induction. No assumption on the size of \(k\) is needed.

**3. Finite periods and minimal components.** Modulo \(3^n\), equation (1) says that \(F^{3^k}(x)=x\) exactly when \(2t+k\ge n\); since one such power of \(3\) is a return, the least return is the smallest such power. In particular every point of \(3R_n\) is periodic. A residue with \(t\ge\lceil n/2\rceil\) is fixed; there are \(3^{\lfloor n/2\rfloor}\) of them. For \(t<n/2\), the number of residues with that exact valuation is \(2\cdot3^{n-t-1}\), and their period is \(3^{n-2t}\). Dividing gives \(2\cdot3^{t-1}\) cycles. Different \(t\) produce different cycle lengths (all exponents \(n-2t\) are distinct), proving the cycle census and zeta expression. The maximal-period count follows by taking \(t=1\) when \(n\ge3\).

Now fix \(t\ge1\). There are exactly \(2\cdot3^{t-1}\) residues \(a\pmod{3^{2t}}\) with \(v_3(a)=t\). Since \(F(x)-x=x^2\) is divisible by \(3^{2t}\) throughout \(B_{t,a}\), each such ball is invariant. At level \(n>2t\), this ball has \(3^{n-2t}\) residues, and by the finite-period formula *each* has an orbit of that full length. Thus every finite quotient of \(B_{t,a}\) is a single cycle and every orbit is dense: \(B_{t,a}\) is minimal. The compatible quotient cycles have sizes \(1,3,3^2,\ldots\), producing a topological conjugacy with the ternary odometer. All nonzero points of \(3\mathbb Z_3\) lie in exactly one of these balls. A \(3\)-adic periodic point must be periodic modulo each \(3^n\), yet (1) gives nonzero displacement after every finite power of three, and all finite reduction periods are powers of three; therefore \(0\) is the only periodic point in \(\mathbb Z_3\). (Alternatively, a period on \(\mathbb Z_3\) would contradict unbounded reduction periods.)

**4. Entire transient tree.** Modulo \(3\), each class \(2\) has depth one and each class \(1\) depth two, because every vertex in \(3R_n\) is periodic. The two bijections from Step 1 give exactly one depth-one predecessor \(u\in2+3R_n\) for each periodic vertex. A depth-two predecessor \(v\in1+3R_n\) of \(u\) solves
\[
(2v+1)^2\equiv4u+1\pmod{3^n}.\tag{2}
\]
Because \(u\equiv2\pmod3\), its parameter \(A=4u+1\) runs bijectively through all residues divisible by \(3\); every root \(w\) of \(w^2=A\) is divisible by \(3\), and \(v=(w-1)/2\) belongs to the required class. If \(A=0\), then \(w^2=0\) has exactly \(3^{\lfloor n/2\rfloor}\) roots. If \(v_3(A)=2r<n\), then \(A=3^{2r}a\), with \(a\) a unit modulo \(3^{n-2r}\); equation (2) has roots iff \(a\equiv1\pmod3\), in which case Hensel lifting of the two square roots modulo \(3\) gives exactly \(2\cdot3^r\) roots modulo \(3^n\). Odd valuation gives no roots. The number of choices of \(A\) with \(v_3(A)=2r\) and \(a\equiv1\pmod3\) is \(3^{n-2r-1}\). This proves the full branch histogram and therefore the graph description. The sum of all leaf indegrees is \(3^{n-1}\), as required by the cardinality of \(1+3R_n\).

## Verification
The supplementary standalone Python checker exhaustively computes every orbit and all depth-two indegrees for \(n=1,\ldots,8\), then checks the predicted cycle histogram, branch histogram, and decomposition of the finite state set. Its output is `VERIFY_OK`. The arbitrary-exponent proof is Steps 1–4, not the eight enumerations. Reproduce using `python3 verify.py` with Python standard library only.

## Relationship to prior work
Durand and Paccaut (2009; freely distributed manuscript in 2012) characterize when a polynomial is minimal on *all* ternary integers; the fixed point here excludes global minimality. Fan and Liao (2010) establish general minimal-component and cycle-lifting machinery for odd primes and a complete *binary* quadratic classification; their Theorem E explicitly treats \(x+x^2\) over \(\mathbb Z_2\), not its ternary finite functional graphs or nonuniform square-root preimage trees. General later polynomial minimal-decomposition results do not, in the inspected available descriptions, state the present exact branch histogram, cycle census, or specific decomposition. The methods overlap with standard Hensel lifting and polynomial iteration; the exact all-level graph and critical branching are the additional conclusions.

## Limitations
Only the polynomial \(F(x)=x+x^2\) at prime \(3\) is classified. Finite computations are checks, not a proof for all \(n\). A prior derivation in unindexed materials cannot be ruled out by targeted searches. The 2015 general power-series decomposition article was accessible through its bibliographic description, not verified page-by-page for this exact example. A separate independent mathematical audit has not been performed.

## References
1. F. Durand and F. Paccaut, *Minimal polynomial dynamics on the set of 3-adic integers*, Bull. London Math. Soc. **41** (2009), 302–314, first published 2009-02-27, doi:10.1112/blms/bdp003; arXiv:1208.2016.
2. A. Fan and L. Liao, *On minimal decomposition of p-adic polynomial dynamical systems*, arXiv:1010.5583v1 (first public 2010-10-27), revised v2 (2010-10-29), especially §§1–2 and Theorem E in §6.
3. A. Fan et al., *Dynamics of convergent power series on the integral ring of a finite extension of \(\mathbb Q_p\)*, J. Differential Equations (2015), doi:10.1016/j.jde.2015.03.042 (general context).
