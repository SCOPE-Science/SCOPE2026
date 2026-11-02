# Exact prime-power attraction-depth transfer for the quadratic critical two-cycle

## Finding
Let \(p\) be any odd prime and let \(k\ge1\). On \(\mathbb Z/p^k\mathbb Z\), iterate
\[f(x)=x^2-1.\]
The residues \(0,-1\) form a two-cycle. For each \(r\in\mathbb F_p\), define the first hitting time
\[\tau_p(r)=\min\{j\ge0:f^j(r)=0\text{ in }\mathbb F_p\},\]
when this minimum exists. Let \(B_p\) be the set of such residues, and put
\[T_p(z)=\sum_{r\in B_p}z^{\tau_p(r)}.\]
For every \(x\pmod{p^k}\) whose forward orbit eventually reaches the exact cycle \(\{0,-1\}\), let \(d_{p,k}(x)\) be the first-entry time, counting both cycle points as depth zero. Define
\[c_k=\left\lceil\frac{k}{2}\right\rceil,\qquad
h_k(s)=\min\{j\ge0:2^js\ge c_k\}\quad(1\le s<k),\]
\[Q_{p,k}(u)=\sum_{s=1}^{k-1}(p-1)p^{k-s-1}u^{h_k(s)}.\]
For \(k=1\), this last polynomial is zero. Then **the exact first-entry polynomial of the entire attracting basin** is
\[\boxed{H_{p,k}(z):=\sum_{x\,\bmod\,p^k:\,x\bmod p\in B_p}z^{d_{p,k}(x)}
=1-z+T_p(z)\bigl(1+zQ_{p,k}(z^2)\bigr).}\]
In particular, a residue modulo \(p^k\) reaches the cycle if and only if its reduction modulo \(p\) belongs to \(B_p\), and the basin has exactly \(|B_p|p^{k-1}\) vertices. Thus the full finite-level depth census is determined by the finite dynamical graph over \(\mathbb F_p\) and a universal shell polynomial.

The shell polynomial has at most \(1+\lceil\log_2 c_k\rceil\) nonzero terms. Explicitly, with \(J=\lceil\log_2 c_k\rceil\), its coefficient \(W_0\) is \(p^{k-c_k}-1\); for \(1\le j\le J\), set
\[L_j=\left\lceil\frac{c_k}{2^j}\right\rceil,\qquad
U_j=\left\lceil\frac{c_k}{2^{j-1}}\right\rceil-1,\qquad
W_j=p^{k-L_j}-p^{k-U_j-1}.\]
Then \(Q_{p,k}(u)=\sum_{j=0}^{J}W_ju^j\). If \(m_p=\max_{r\in B_p}\tau_p(r)\), the sharp maximum basin depth for \(k\ge2\) equals
\[\boxed{\max d_{p,k}=m_p+1+2\left\lceil\log_2\left\lceil\frac{k}{2}\right\rceil\right\rceil.}\]
For \(k=1\), the maximum is \(m_p\).

The entire ring is attracted when \(p=3\) or \(p=7\). Here
\[T_3(z)=1+2z,\qquad T_7(z)=1+2z+2z^2+2z^3.\]
Consequently, for \(k\ge2\), the exact largest transient is \(2+2\lceil\log_2\lceil k/2\rceil\rceil\) at \(p=3\), and \(4+2\lceil\log_2\lceil k/2\rceil\rceil\) at \(p=7\). In contrast, at \(p=5\), only \(3\cdot5^{k-1}\) of the \(5^k\) states lie in this cycle's basin; there \(T_5(z)=1+2z\).

## Assumptions and scope
All calculations are in the finite rings \(\mathbb Z/p^k\mathbb Z\) for odd rational primes \(p\) and positive integers \(k\). Reduction modulo \(p\) is always taken before the first-hitting time \(\tau_p\). The polynomial \(H_{p,k}\) counts **only** the basin of the distinguished critical two-cycle; it makes no assertion that this is the only cycle for an arbitrary odd prime. The logarithm in the maximum formula has base two. Valuation shells and their counts refer to residues in one fixed congruence class modulo \(p\).

## Proof
**(1) Reduction identifies the basin.** The identities \(f(0)=-1\) and \(f(-1)=0\) give the distinguished two-cycle in every ring. Since reduction commutes with iteration, a state reaching the exact cycle must reduce to a residue in \(B_p\). Conversely, the remaining proof establishes that every residue lifting an element of \(B_p\) does reach this cycle.

**(2) Canonical lift of each finite-field first-hit orbit.** Fix \(r\in B_p\) and write \(t=\tau_p(r)\). The polynomial \(F_r=f^t\) satisfies \(F_r(r)=0\pmod p\). For \(t>0\), its derivative is
\[F'_r(r)=\prod_{i=0}^{t-1}2f^i(r)\not\equiv0\pmod p,\]
because the finite-field orbit first encounters zero at step \(t\), and \(p\) is odd. The same holds for \(t=0\), when \(F_r(X)=X\). Hensel's lemma gives a unique \(\rho_r\in r+p\mathbb Z_p\) with \(F_r(\rho_r)=0\). The derivative remains a unit throughout that residue ball. Polynomial factorization of the difference therefore gives the **exact local isometry**
\[\nu_p\bigl(F_r(x)\bigr)=\nu_p(x-\rho_r)\]
for all \(x\equiv r\pmod p\). This identity remains valid after reduction modulo \(p^k\), with valuations truncated at \(k\).

**(3) Exactly one exceptional point per residue ball.** Modulo \(p^k\), the unique lift \(\rho_r\) reaches zero at step \(t\). It cannot reach the two-cycle earlier, except when \(r=-1\), where \(t=1\) but \(\rho_r=-1\) already lies on the cycle. Indeed, the sole preimage of \(-1\) in \(\mathbb F_p\) under \(f\) is \(0\), so an orbit that first reaches zero at step \(t\) cannot previously visit \(-1\) unless it started at \(-1\). Hence the contributions of all exceptional lifts form \(T_p(z)-z+1\).

**(4) Exact tail time in the zero residue ball.** Suppose \(y\equiv0\pmod p\) is nonzero modulo \(p^k\), with \(s=\nu_p(y)\in\{1,\ldots,k-1\}\). The algebraic identity
\[f^2(y)=y^2(y^2-2)\]
and the fact that \(p\) is odd imply \(\nu_p(f^2(y))=2\nu_p(y)\), until the valuation reaches \(k\). The first point at which applying \(f\) yields exactly \(-1\) is the first even iterate whose valuation is at least \(c_k=\lceil k/2\rceil\). At the preceding even iterates the valuation is strictly below \(c_k\), so neither element of the cycle has yet appeared. The first-entry time from \(y\) is therefore precisely \(2h_k(s)+1\). An overshoot to zero cannot occur before this entry: doubling a positive integer smaller than \(c_k\) gives a number below \(k\).

**(5) Shell counting and convolution.** For any fixed \(r\pmod p\), exactly one residue modulo \(p^k\) is congruent to the canonical lift \(\rho_r\). For each \(1\le s<k\), exactly \((p-1)p^{k-s-1}\) other residues satisfy \(\nu_p(x-\rho_r)=s\). By (2), these reach a nonzero zero-class state after \(t\) steps; by (4), their total first-entry depth is \(t+1+2h_k(s)\). Their contribution is \(z^t zQ_{p,k}(z^2)\). Summing over \(r\in B_p\) and adjoining the exceptional lifts in (3) proves the boxed identity. Summing coefficients at \(z=1\) gives \(|B_p|p^{k-1}\), proving exact basin membership.

**(6) Compressed shells and maximum.** The shell \(h_k(s)=0\) consists of \(c_k\le s<k\), giving \(W_0=p^{k-c_k}-1\). For \(j\ge1\), the shell boundaries are \(L_j\le s\le U_j\), giving \(W_j=p^{k-L_j}-p^{k-U_j-1}\) by a geometric sum. For \(k\ge2\), the shell \(s=1\) is present and has maximal \(h_k(1)=\lceil\log_2 c_k\rceil\), so the largest depth comes from a residue \(r\) with \(\tau_p(r)=m_p\), and equals the stated maximum. For \(k=1\), \(Q_{p,1}=0\) and \(T_p-z+1\) has largest degree \(m_p\), since \(1\) and \(-1\) are distinct and both have \(\tau_p=1\).

Finally, direct finite-field squaring verifies the displayed \(T_p\) for \(p\in\{3,5,7\}\). In particular every residue modulo \(3\) or \(7\) reaches the critical cycle, whereas modulo \(5\) the residues \(2,3\) lie outside its basin.

## Verification
A standalone exact-integer verifier (`verify.py`) independently enumerates the finite-field basin, predicts the entire histogram by the theorem, and iterates every residue in that basin modulo \(p^k\) until reaching the two-cycle, without using the valuation proof as its traversal algorithm. It asserts equality of all histogram coefficients and the predicted total basin size. The recorded replay covers \(43\) prime/level pairs across \(p=3,5,7,11,13,17,19\) and directly examines \(1,696,943\) residue states in their full rings. See `VERIFICATION.md` for the reproducible command and exact replay output. All general statements are proved symbolically; finite tests alone are not a proof for arbitrary primes or levels.

## Relationship to prior work
Fan and Liao (arXiv:1010.5583, 2010) establish broad minimal decomposition and lifting principles for \(p\)-adic polynomial dynamics, with an explicit classification of quadratic systems in the **dyadic** case. Nevins and Rogers study qualitative basins and periodic points of quadratic maps over \(p\)-adic fields, including maps whose parameter has unit norm. Fan and Liao (arXiv:1408.4574, 2014) study the distinct squaring map \(x\mapsto x^2\). The present statement gives a uniform, exact **finite-level first-entry generating polynomial** for the specific critical two-cycle under \(x\mapsto x^2-1\), for **every odd prime** and every prime-power modulus, including a sharp maximum and complete-basin consequences. It does not claim to originate the general Hensel lifting mechanism or qualitative attracting-cycle principle.

## Limitations
This is a complete census of one attracting basin, not a complete census of other periodic cycles that may exist for particular primes. No distribution of transient lengths outside that basin is asserted. For the special primes \(3\) and \(7\), the basin is the full ring. Existing general lifting theory could implicitly imply parts of the proof; equivalent numerical depth formulas in sources not found during the literature comparison cannot be excluded.

## References
1. A.-H. Fan and L. Liao, *On minimal decomposition of p-adic polynomial dynamical systems*, arXiv:1010.5583v1 (first submitted 2010-10-27), §2 and §6; Advances in Mathematics 228 (2011). https://arxiv.org/abs/1010.5583
2. M. Nevins and T. D. Rogers, *Quadratic maps as dynamical systems on the p-adic numbers*, manuscript dated 2000-03-22, especially §5 (accessible copy with imperfect text extraction). https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/nevins.pdf
3. S. Fan and L. Liao, *Dynamics of the square mapping on the ring of p-adic integers*, arXiv:1408.4574v1 (2014-08-20). https://arxiv.org/abs/1408.4574
