# Möbius-ladder parity dynamics: exact transient shells and Jordan-chain fusion under a twist

## Finding

For each integer \(n\ge3\), let \(M_{2n}\) be the simple Möbius ladder with labelled vertex set \(\mathbb Z/(2n)\mathbb Z\), edges joining \(i\) to \(i-1\), \(i+1\), and \(i+n\). The synchronous neighbor-XOR map \(F_n\) acts on all \(2^{2n}\) configurations over \(\mathbb F_2\), with no self-feedback. Define \(\tau(x)\) as the least \(j\ge0\) such that \(F_n^j(x)\) is periodic, and set \(e=2^{\nu_2(n)}\).

**Exact first-periodic-entry census.** If \(3\nmid n\), every configuration is periodic from time zero. If \(3\mid n\), exactly
\[
P_n=2^{2n-4e}
\]
configurations are periodic. When \(n\) is odd, precisely \(P_n\) configurations have \(\tau=0\) and \(15P_n\) have \(\tau=1\). When \(n\) is even, precisely \(P_n\) have \(\tau=0\), and
\[
\#\{x:\tau(x)=j\}=3P_n4^{j-1}\qquad(1\le j\le 2e).
\]
There are no other entry times. Every stated maximal transient time is attained.

**Full nilpotent structure.** When \(3\mid n\), the nilpotent primary summand of \(F_n\) consists of four Jordan blocks of size one if \(n\) is odd, and exactly two blocks of size \(2e\) if \(n\) is even. Its dimension is always \(4e\). For the untwisted prism \(C_n\square K_2\), the corresponding nilpotent partitions instead are two size-two blocks when \(n\) is odd and four size-\(e\) blocks when \(n\) is even. Thus twisting preserves the number of periodic configurations and the divisibility-by-three reversibility criterion, but splits the odd-case Jordan chains and fuses the even-case Jordan chains. In the even case the maximal transient is doubled; in the odd case it is halved.

**Fixed and primitive periodic orbits.** The exact number of fixed configurations is
\[
\#\operatorname{Fix}(F_n)=
\begin{cases}
2,&n\text{ odd},\\
8,&n\equiv2\pmod4,\\
4,&n\equiv0\pmod4.
\end{cases}
\]
Put \(H_n(z)=z^{2n}+1\) and \(Q_n(z)=z^{n+1}+z^2+1\) in \(\mathbb F_2[z]\). For every positive integer \(t\),
\[
\#\operatorname{Fix}(F_n^t)=
2^{\deg\gcd(H_n(z),Q_n(z)^t+z^t)}.
\]
Consequently, for every positive integer \(d\), the exact number of distinct primitive \(d\)-cycle orbits (without identifying spatial symmetries) is
\[
\frac1d\sum_{t\mid d}\mu(d/t)\,
2^{\deg\gcd(H_n(z),Q_n(z)^t+z^t)}.
\]
This last expression is an exact finite polynomial-arithmetic census, not a claim that every \(d\) is realized. As a supplementary explicit family, when \(n=2^k\ge4\) all states are periodic, the map has exact order \(n\), and \(\#\operatorname{Fix}(F_n^t)=2^{\min(2^{\nu_2(t)+1},2n)}\).

## Assumptions and scope

All operations are over the binary field. Vertices and configurations are labelled, edges are undirected, and the update is synchronous. The graph contains exactly three different neighbors per vertex because \(n\ge3\). Periodic means belonging to a cycle at the initial state, not merely eventually reaching one. First-entry times are absolute nonnegative integers, including zero. The nilpotent partition refers only to the zero-primary component of the linear map; other spectral components are invertible. The polynomial \(\mu\) in the cycle formula is the classical number-theoretic Möbius function.

## Proof

**1. Cyclic representation and the unique obstruction.** Write
\[
R_n=\mathbb F_2[z]/(z^{2n}+1),\qquad
f_n(z)=z+z^{-1}+z^n.
\]
Since \(z^{2n}=1\) in this ring, the synchronous update is exactly multiplication by \(f_n\). Multiplying by the unit \(z\) replaces its numerator by \(Q_n=z^2+1+z^{n+1}\).

Write \(n=em\) with \(m\) odd and \(e\) a power of two. Then \(z^{2n}+1=(z^m+1)^{2e}\), with \(z^m+1\) square-free. If \(\alpha\) is any root of \(z^{2n}+1\) in an algebraic closure, then \(\alpha^n=1\). Hence \(f_n(\alpha)=\alpha+\alpha^{-1}+1\). It vanishes if and only if \(\alpha\) satisfies \(h(\alpha)=0\), where
\[
h(z)=z^2+z+1.
\]
The two roots of \(h\) are primitive cubic roots, so they occur precisely when \(3\mid n\). Therefore \(F_n\) is invertible exactly when \(3\nmid n\); a bijection of a finite set makes every configuration periodic.

**2. Local multiplicity and nilpotent Jordan blocks.** Suppose \(3\mid n\). The irreducible polynomial \(h\) appears with exponent \(2e\) in \(H_n\). The Chinese remainder theorem splits \(R_n\) into the primary factor \(R_h=\mathbb F_2[z]/(h^{2e})\) and a complementary ring on which multiplication by \(f_n\) is invertible. Every periodic configuration must have zero \(R_h\) component, because a nilpotent map has no nonzero periodic state.

If \(n\) is odd, \(e=1\), and the derivative \(Q_n'(z)\) vanishes identically. Since \(h\mid Q_n\) and \(h\) is separable, \(h^2\mid Q_n\). Thus multiplication by \(f_n\) is identically zero on \(R_h=\mathbb F_2[z]/(h^2)\). Its four binary dimensions form four size-one nilpotent Jordan blocks.

If \(n\) is even, \(Q_n'(z)=z^n\). This is nonzero at every root of \(h\), so \(h\) divides \(Q_n\) to multiplicity exactly one. Multiplication by \(f_n\) on \(R_h\) is multiplication by \(h\) times a unit. For each \(j\ge0\), the kernel of its \(j\)-th power has size
\[
\#\ker(F_n^j|_{R_h})=2^{2\min(j,2e)}.
\]
Because successive kernel dimensions rise by two until \(j=2e\), the Jordan partition is exactly two size-\(2e\) blocks. The local binary dimension is \(4e\) in either parity case. This proves the exact periodic-state count \(P_n=2^{2n-4e}\).

**3. Transient shells.** A state enters the periodic set by time \(j\) if and only if its nilpotent primary component lies in \(\ker F_n^j\). Its complementary invertible coordinate can be chosen in exactly \(P_n\) ways. For odd \(n\), the nilpotent restriction is zero, so all \(2^4\) local states enter by step one. For even \(n\), the number entering by time \(j\) is \(P_n2^{2\min(j,2e)}\). Subtracting consecutive cumulative totals yields the formula \(3P_n4^{j-1}\) for \(1\le j\le2e\), with sharpness because every difference is positive. The counts sum to \(2^{2n}\).

**4. Untwisted-prism comparison, derived independently.** On the prism \(C_n\square K_2\), use \(R=\mathbb F_2[z]/(z^n+1)\) and \(s=z+z^{-1}\). The two-layer matrix \(\left(\begin{smallmatrix}s&1\\1&s\end{smallmatrix}\right)\) is similar over \(R\) to \(\left(\begin{smallmatrix}b&1\\0&b\end{smallmatrix}\right)\), where \(b=s+1=z^{-1}h\). At the \(h\)-primary factor \(\mathbb F_2[z]/(h^e)\), when \(e=1\), this is a size-two nilpotent Jordan block over \(\mathbb F_4\), or two size-two blocks over \(\mathbb F_2\). When \(e\ge2\), its \(j\)-th power for even \(j\) is diagonal with \(b^j\) twice, yielding binary kernel dimension \(4\min(j,e)\). For odd \(j\), the local Smith invariants are \(b^{j-1}\) and \(b^{j+1}\); since \(e\) is even, they give the same dimension \(4\min(j,e)\). The nilpotent partition is consequently four size-\(e\) blocks. The total dimension remains \(4e\), but its block lengths differ as asserted.

**5. Fixed states and complete primitive-census formula.** The kernel of multiplication by any \(g\) on \(\mathbb F_2[z]/(H_n)\) has binary dimension \(\deg\gcd(g,H_n)\). Multiplying \(f_n^t+1\) by the unit \(z^t\) gives \(Q_n^t+z^t\). This proves the fixed-time formula, and Möbius inversion of the counts of period dividing \(d\) proves the primitive-cycle formula.

For the single-step fixed states, a root \(\alpha\) of \(H_n\) is also a root of \(f_n+1\) exactly when \(\alpha+\alpha^{-1}=0\), or \(\alpha=1\). Thus only the \(z+1\)-primary component contributes. Using
\[
z(f_n+1)=(z+1)^2+z(z^n+1),
\]
its \(z+1\)-valuation is one when \(n\) is odd, three when \(\nu_2(n)=1\), and two when \(\nu_2(n)\ge2\). For the middle case, write \(n=2m\) with \(m\) odd and \(H=(z^m+1)/(z+1)\). Then the displayed expression is \((z+1)^2(1+zH^2)\), and the final factor has a simple root at \(z=1\), since \(H(1)=1\) and its derivative at one is one. In the other cases the distinct lowest valuations preclude cancellation. Each valuation is below the multiplicity \(2e\) of \(z+1\) in \(H_n\), giving exactly \(2\), \(8\), or \(4\) fixed states.

Finally, for \(n=2^k\ge4\), the only irreducible factor of \(H_n\) is \(z+1\), and \(F_n+I\) is multiplication by \((z+1)^2\) times a unit. There are therefore two Jordan blocks of size \(n\) with eigenvalue one. The characteristic-two identity \((I+N)^{2^r}=I+N^{2^r}\) yields the supplementary fixed counts and the sharp global order \(n\).

## Verification

The standalone script `verify_mobius_xor.py` directly builds every binary update matrix for \(3\le n\le48\) and independently checks all predicted ranks of powers. It compares exact matrix nullities of \(F_n^t+I\) with the polynomial-gcd formula, checks the single-step fixed-state trichotomy, and independently verifies prism comparison dimensions. A separate complete functional-graph calculation classifies every configuration for \(3\le n\le8\), checking the distribution of first entry times without relying on polynomial formulas.

The recorded test passed 1,115 matrix-kernel and gcd cases, 429 independent prism matrix cases, and 87,360 exhaustively classified binary states. Run `python verify_mobius_xor.py` using Python 3; no external packages or data files are required. These finite checks support but do not replace the general algebraic proof.

## Relationship to prior work

Martin, Odlyzko and Wolfram (1984) developed polynomial methods for finite linear cellular automata. Nordahl (1989) explicitly identified the divisibility-by-three obstruction for the *ordinary* cyclic Rule 150 automaton. Tadaki (1993) studied period and relaxation of Rule 90 and Rule 150 with Dirichlet boundaries. Zaidenberg (2006) analyzed convolution operators and periodic binary harmonic functions on lattices. These supply relevant algebraic and dynamical background but do not, in the examined material, give the nilpotent Jordan partitions, entry-time populations or Möbius-versus-prism chain-fusion phenomenon for the antipodally coupled \(2n\)-cycle.

An earlier exact prism neighbor-XOR classification establishes the untwisted transient shells; the new twisted-graph calculation is not its special case because a Möbius identification changes the characteristic-two local Jordan structure. In particular, both models share the same periodic fraction \(2^{-4e}\) for \(3\mid n\), yet their nilpotent Jordan partitions and maximal transient times are different. General cyclic-polynomial methods can compute either system instance by instance; they do not constitute the stated all-length, explicit twist comparison without the factor-multiplicity argument above.

## Limitations

The result concerns binary synchronous nearest-neighbor XOR only, not majority dynamics, asynchronous updates, higher characteristic or weighted rungs. The gcd formula determines every periodic orbit count algorithmically but is not a closed elementary expression for the global permutation order at arbitrary non-dyadic \(n\). Literature searches cannot establish absolute absence of historical equivalent formulations. Independent expert evaluation has not been performed.

## References

- O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. https://doi.org/10.1007/BF01223745
- M. G. Nordahl, *Formal Languages and Finite Cellular Automata*, Complex Systems **3** (1989), 63–78. https://wpmedia.wolfram.com/uploads/sites/13/2018/02/03-1-5.pdf
- S.-i. Tadaki, *Orbits in one-dimensional finite linear cellular automata*, arXiv:cond-mat/9305012v1 (first posted 1993-05-14). https://arxiv.org/abs/cond-mat/9305012
- M. Zaidenberg, *Convolution equations on lattices: periodic solutions with values in a prime characteristic field*, arXiv:math-ph/0606070v1 (first posted 2006-06-29). https://arxiv.org/abs/math-ph/0606070
