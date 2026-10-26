# A prime-power period law for finite truncations of a triangular cellular automaton

## Finding

Let \(p\) be prime, \(L,m\) positive integers, and let \(A_{L,m}\) act on \((\mathbb F_p^{m+1})^{\mathbb Z/L\mathbb Z}\) by
\[
(A_{L,m}x)_0(g)=x_0(g),\qquad
(A_{L,m}x)_j(g)=x_j(g+1)-x_{j-1}(g)\quad(1\le j\le m).
\]
Write \(L=p^a d\), where \(p\nmid d\), and put \(q=p^a\). The **least positive period of this permutation of its entire configuration space** is exactly
\[
\operatorname{ord}(A_{L,m})
=d\,p^{\lceil\log_p(m+q)\rceil}.
\]
Equivalently, \(A_{L,m}^{d p^e}\) is the identity if and only if \(p^e\ge m+p^a\). The condition \(m\ge1\) is essential; at \(m=0\) the map is the identity. In particular, at fixed \(L\) the periods diverge with \(m\); the coordinatewise inverse-limit automorphism on \(((\mathbb F_p)^{\mathbb N_0})^{\mathbb Z/L\mathbb Z}\) has infinite order, although every finite-layer quotient has finite order.

## Assumptions and scope

All indices \(g\) are taken modulo \(L\); the shift \(S\) sends a scalar configuration \(v(g)\) to \(v(g+1)\). The coefficient-index \(j\) ranges from \(0\) to \(m\). The map is upper- or lower-triangular according to coordinate ordering, with invertible diagonal blocks, so it is a bijection. No probabilistic initial-state assumption is used. \(\operatorname{ord}\) means the least positive \(t\) such that \(A_{L,m}^t\) fixes **every** configuration, not the period of one configuration. For \(m\ge1\) the formula covers every spatial length \(L\ge1\), including \(p\mid L\).

## Proof

Identify scalar configurations with \(R=\mathbb F_p[z]/(z^L-1)\), where \(S\) is multiplication by \(z\). The matrix of \(A_{L,m}\) on \(R^{m+1}\) is bidiagonal with first diagonal block \(1\), the other \(m\) diagonal blocks \(z\), and entries \(-1\) immediately below the diagonal. It is invertible since \(z\) is a unit in \(R\).

Over an algebraic closure, factor \(z^L-1=(z^d-1)^{p^a}\). Because \(p\nmid d\), the factors associated with distinct \(d\)-th roots \(\lambda\) are coprime. The resulting local ring for each root is \(\overline{\mathbb F}_p[b]/(b^q)\) with \(z=\lambda+b\). The eigenvalues of the whole automorphism are \(1\) and every \(d\)-th root (the latter occur because \(m\ge1\)). Hence its order has prime-to-\(p\) part exactly \(d\), and the remaining part is some power of \(p\).

In the local factor \(\lambda=1\), write \(A=I+N\). The matrix \(N\) has diagonal \(0,b,\ldots,b\) and subdiagonal \(-1\). Direct matrix-path enumeration gives, for \(1\le j\le m\) and \(k\ge j\),
\[
 (N^k)_{j,0}=(-1)^j\binom{k-1}{j-1}b^{k-j},
\]
with \((N^k)_{j,0}=0\) if \(k<j\). Entries from a positive-index source \(i\ge1\) to \(j\ge i\) are
\[
 (N^k)_{j,i}=(-1)^{j-i}\binom{k}{j-i}b^{k-(j-i)}
\]
when \(k\ge j-i\), and vanish otherwise. These expressions follow by choosing the positions of the required downward steps among \(k\) factors, noting that a path starting at column zero must leave column zero before any diagonal multiplication is possible.

Set \(k=p^e\). In characteristic \(p\), every binomial coefficient \(\binom{k}{r}\) with \(0<r<k\) vanishes; by the base-\(p\) digit criterion, every \(\binom{k-1}{j-1}\) with \(1\le j\le k\) is nonzero modulo \(p\). If \(k<m\), the entry \((N^k)_{k,0}=(-1)^k\) is nonzero. If \(m\le k<m+q\), the entry \((N^k)_{m,0}=(-1)^m\binom{k-1}{m-1}b^{k-m}\) is nonzero because \(0\le k-m<q\). If \(k\ge m+q\), all entries of \(N^k\) vanish: positive-column offdiagonal terms have zero binomial coefficients, diagonal powers \(b^k\) vanish, and every column-zero term contains at least \(b^q\). Thus \(N^{p^e}=0\) **exactly** when \(p^e\ge m+q\). By Frobenius, \((I+N)^{p^e}=I+N^{p^e}\).

For \(\lambda\ne1\), the zeroth coordinate block of \(A\) has eigenvalue \(1\), whereas its positive-index block \(B=(\lambda+b)I-J\) (with \(J\) the nilpotent lower shift of size \(m\)) has eigenvalue \(\lambda\). Since \(B-I\) is invertible in the local ring, a triangular similarity removes the coupling from coordinate zero. When \(p^e\ge m+q\), we have \(J^{p^e}=0\) and \(b^{p^e}=0\). Therefore \(B^{p^e}=\lambda^{p^e}I\), and \(B^{d p^e}=I\). The zeroth block is already the identity. The \(\lambda=1\) block gives the **necessary** lower bound on \(e\); the other blocks introduce no larger \(p\)-power. This proves the stated exact order.

For fixed \(L\), if the inverse-limit map had finite order \(t\), all its finite-coordinate quotients would have order dividing \(t\). The displayed orders grow unboundedly with \(m\), a contradiction.

## Verification

Run `python3 CHECK.py`. It constructs the exact configuration matrix over \(\mathbb F_p\), checks the proposed power is the identity, and checks every prime divisor of the candidate order to establish minimality in 135 finite cases (\(p\in\{2,3,5\}\), \(L\le8\), \(m\le6\), with matrix dimension at most 45). `CHECK_OUTPUT.txt` records the actual run. These tests support but do not establish the theorem for unbounded parameters; that is the role of the preceding proof.

## Relationship to prior work

J. Yang, *A Closed Image Characterization of Locally Finite Groups via Linear Cellular Automata* (arXiv:2606.22740v1, Section 3, Eq. (6)), introduced the countable-coordinate triangular rule for a distinct non-closed-image problem. A. Castillo-Ramirez, *A characterization of the reversibility of linear cellular automata* (arXiv:2608.20600v1, Section 4, Eqs. (5)–(6)), extends its direct-sum construction to a bijective, non-reversible automaton on a product alphabet. The statement here concerns the **exact temporal permutation order of every finite inner-coordinate quotient on a finite spatial cycle**, which neither cited construction establishes. Related work on periodic cellular-automaton dynamics exists, and unrestricted priority is not claimed.

## Limitations

The theorem is specific to the constant spatial step and the indicated triangular coefficients over a prime field; it does not determine the order for arbitrary nonconstant step sequences, composite coefficient rings, or unrelated reversible cellular automata. It describes whole-state permutation order, not the distribution of individual orbit lengths. Finite computational checks cover only listed parameter cases. Bibliographic searches do not establish absolute novelty; older general finite-order methods might imply the result after specializing and calculating their invariants.

## References

1. J. Yang, *A Closed Image Characterization of Locally Finite Groups via Linear Cellular Automata*, arXiv:2606.22740v1 (first submitted 2026-06-22). https://arxiv.org/abs/2606.22740
2. A. Castillo-Ramirez, *A characterization of the reversibility of linear cellular automata*, arXiv:2608.20600v1 (first submitted 2026-08-20). https://arxiv.org/abs/2608.20600
3. H. Aso, *Dynamical characteristics of linear cellular automata*, J. Comput. System Sci. 30 (1985), 291–317, DOI 10.1016/0022-0000(85)90048-0 (background on finite-order dynamics; full text not inspected).
