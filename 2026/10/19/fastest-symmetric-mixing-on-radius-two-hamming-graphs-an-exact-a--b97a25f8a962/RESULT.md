# Fastest symmetric mixing on radius-two Hamming graphs: an exact alphabet–dimension phase diagram

## Finding

Let \(q,d\) be integers at least \(2\). On the vertex set \(\{0,\ldots,q-1\}^{d}\), join two distinct vertices whenever their Hamming distance is \(1\) or \(2\). Every undirected edge and every vertex holding probability may initially be chosen independently. Among **all** symmetric entrywise-nonnegative stochastic transition matrices supported on this graph and its diagonal, minimize the second-largest eigenvalue modulus (SLEM) \(\mu(P)=\|P-J/q^d\|_2\), where \(J\) is the all-ones matrix.

Put \(u=q-1\), \(N_1=du\), and \(N_2=\binom d2u^2\). The following table gives an optimal total probability \(a\) of moving a Hamming distance \(1\), total probability \(b\) of moving a distance \(2\), holding probability \(h\), and the **globally minimum** SLEM \(\mu_*\). Each outgoing edge at distance \(1\) receives probability \(a/N_1\), and each at distance \(2\) receives \(b/N_2\).

| Range | \(a\) | \(b\) | \(h\) | \(\mu_*\) |
|---|---|---|---|---|
| \(d=2\), \(q\ge2\) | \(2u/q^2\) | \(u^2/q^2\) | \(1/q^2\) | \(0\) |
| \(d=3\), \(2\le q\le4\) | \(6u(4-q)/(7q^2)\) | \(12u^2/(7q^2)\) | \((q^2-6q+12)/(7q^2)\) | \(1/7\) |
| \(d=3\), \(q\ge5\) | \(0\) | \(1\) | \(0\) | \((q-3)/(3u)\) |
| \(d\ge4\), \(q=2\) | \(2/(d+1)\) | \((d-1)/(d+1)\) | \(0\) | \((d-3)/(d+1)\) |
| \(d\ge4\), \(q\ge3\) | \(0\) | \(1\) | \(0\) | \(1-2q/(du)\) |

In this distance-orbit-invariant subclass the optimum is unique, except that uniqueness is not asserted over the fully unrestricted edge-weight space. For \(d=2\), the unrestricted optimum is uniquely the uniform complete-graph kernel.

The phase transitions are sharp. At \(d=3\), distance-one moves disappear exactly when \(q\ge4\), but holding remains necessary at \(q=4\); holding disappears exactly when \(q\ge5\). For every \(d\ge4\), holding disappears; for binary alphabets, the optimum is uniform on *all* distance-one and distance-two edges, whereas for \(q\ge3\) the optimum uses only distance-two edges.

For every \(q\ge2\) and \(d\ge4\), the best possible spectral gap \(1-\mu_*\) is **exactly twice** the best spectral gap when only distance-one edges and loops are allowed. This is a comparison of optimal SLEM spectral gaps, not a claim about equal computational cost or total-variation mixing at each finite time.

## Assumptions and scope

The Hamming alphabet may have any integer size \(q\ge2\); a finite-field structure is not required. The ambient graph has \(q^d\) vertices, is undirected, and has no restrictions on individual edge probabilities apart from symmetry, nonnegativity, row stochasticity, and the stated support. The convention for spectral mixing includes every eigenvalue orthogonal to constants in absolute value. Each vertex has a permitted self-loop. Nonuniqueness of possible unrestricted optimizers is not ruled out; only the existence of the displayed global optimizer and uniqueness inside the two-orbit invariant subclass are proved.

## Proof

**1. Reduction without assuming equal weights.** The group of independent alphabet permutations in each coordinate, together with coordinate permutations, preserves the graph and is transitive on ordered pairs at each fixed Hamming distance. Average any admissible symmetric stochastic matrix \(P\) over this finite group. The average is admissible, and convexity of the operator norm on the subspace orthogonal to constants gives

\[\|\overline P-J/q^d\|_2\le \|P-J/q^d\|_2.\]

Therefore a global optimum exists among matrices \(P=hI+(a/N_1)A_1+(b/N_2)A_2\), where \(A_i\) is the distance-\(i\) adjacency matrix, \(a,b,h\ge0\), and \(a+b+h=1\).

**2. Exact full spectrum.** Regard the alphabet as the cyclic group \(\mathbb Z/q\mathbb Z\) for Fourier diagonalization only. A character with \(k\) nontrivial coordinate factors, \(0\le k\le d\), has normalized distance-one and distance-two eigenvalues

\[F_1(k)=1-\frac{qk}{ud},\qquad F_2(k)=1-\frac{2qk}{ud}+\frac{q^2k(k-1)}{u^2d(d-1)}.\]

Indeed, the sum of a nontrivial character over the \(u\) nonzero coordinate displacements is \(-1\). Choosing one or two displaced coordinates gives these expressions, including every multiplicity of the spectrum. Thus

\[\lambda_k=h+aF_1(k)+bF_2(k),\qquad 0\le k\le d,\]

where \(\lambda_0=1\), and \(\mu(P)=\max_{1\le k\le d}|\lambda_k|\).

**3. The complete graph \(d=2\).** Every pair of distinct vertices differs in at most two coordinates. Hence \(P=J/q^2\) is feasible and has SLEM zero. A symmetric stochastic kernel with SLEM zero acts as identity on constants and vanishes on their orthogonal complement, so it must equal \(J/q^2\).

**4. Three coordinates.** All \(\lambda_k\) form a quadratic polynomial in \(k\); thus its Lagrange interpolation identity at \(0,1,2,3\) is

\[1=3\lambda_1-3\lambda_2+\lambda_3.\]

Consequently \(\mu\ge1/7\). Equality forces \((\lambda_1,\lambda_2,\lambda_3)=(1,-1,1)/7\). Solving the first two linear equations gives

\[a=\frac{6u(4-q)}{7q^2},\quad b=\frac{12u^2}{7q^2},\quad h=\frac{q^2-6q+12}{7q^2}.\]

All three masses are nonnegative precisely for \(2\le q\le4\); substitution gives the required third contact. For \(q\ge5\), the \(k=1\) spectral mode yields

\[\lambda_1=1-\frac{q}{3u}(a+2b)\ge1-\frac{2q}{3u}=\frac{q-3}{3u}.\]

Take \(a=h=0,b=1\). Its three nontrivial eigenvalues are

\[\frac{u-2}{3u},\quad -\frac{2u-1}{3u^2},\quad \frac1{u^2}.\]

For \(u\ge4\) the first dominates the other two in absolute value: the respective comparison differences are \((u^2-4u+1)/(3u^2)>0\) and \((u-3)(u+1)/(3u^2)>0\). This reaches the lower bound.

**5. Binary alphabet in dimensions \(d\ge4\).** Here \(F_1(1)=1-2/d\), \(F_2(1)=1-4/d\), \(F_1(d)=-1\), and \(F_2(d)=1\). For all admissible masses,

\[\lambda_1=1-\frac{2a+4b}{d}\ge1-\frac4d+\frac{2a}{d},\qquad \lambda_d=1-2a.\]

The maximum of the two displayed lower bounds is at least \((d-3)/(d+1)\), with equality only if \(a=2/(d+1)\) and \(b=1-a\). For this choice the entire nontrivial spectrum is

\[\lambda_k=1-\frac{4k(d-k+1)}{d(d+1)}.\]

This convex quadratic has maximum \((d-3)/(d+1)\) on the integer interval \(1\le k\le d\), attained at both endpoints. Its minimum is \(-1/(d+1)\) when \(d\) is even and \(-1/d\) when \(d\) is odd. These magnitudes do not exceed \((d-3)/(d+1)\) for the specified dimensions. Thus the lower bound is attained, with unique orbit-invariant allocation. For \(q=2\) the optimal per-edge weights for distance one and two are both \(2/[d(d+1)]\).

**6. Nonbinary alphabets in dimensions \(d\ge4\).** The \(k=1\) mode gives, for \(u\ge2\),

\[\lambda_1=1-\frac{q}{du}(a+2b)\ge L:=1-\frac{2q}{du}>0.\]

Choose \(a=h=0,b=1\). Its nontrivial spectrum is \(F_2(k)\), a convex quadratic in \(k\), so its maximum occurs at \(k=1\) or \(k=d\). Now \(F_2(1)=L\) and \(F_2(d)=1/u^2\le L\), since \(d(u-1)\ge2u\). To control the minimum for \(d\ge5\), write

\[F_2(k)=\frac{(ud-qk)^2-[u^2(d-k)+k]}{u^2d(d-1)}\ge-\frac1{d-1}\ge-L.\]

The last inequality holds because \(L\ge1-3/d\ge1/(d-1)\) for \(d\ge5\). For \(d=4\), the four values, in order, are

\[\frac{u-1}{2u},\quad\frac{u^2-4u+1}{6u^2},\quad-\frac{u-1}{2u^2},\quad\frac1{u^2}.\]

Direct comparison shows that all their absolute values are at most the first for every \(u\ge2\); explicitly \((u-1)/(2u)\pm(u^2-4u+1)/(6u^2)\ge0\), and \((u-1)/(2u)\ge (u-1)/(2u^2),1/u^2\). Thus \(\mu=L\), attaining the lower bound, with the only orbit-invariant optimal allocation \(a=h=0,b=1\).

**7. Exact doubling of the spectral gap.** When only distance-one moves are permitted, the Fourier spectrum is \(\lambda_k=1-aqk/(du)\) with \(0\le a\le1\). For \(q\ge3,d\ge4\), the \(k=1\) bound is minimized by \(a=1\), and at that choice its magnitude dominates the \(k=d\) endpoint, giving optimal SLEM \(1-q/(du)\). For \(q=2\), balancing the endpoints gives the known optimal SLEM \((d-1)/(d+1)\). Comparison with parts 5–6 proves

\[\frac{1-\mu_{\mathrm{radius\,2}}}{1-\mu_{\mathrm{radius\,1}}}=2\quad(d\ge4,\ q\ge2).\]

The lower-bound contacts in parts 4–6 also determine the unique optimal \((a,b,h)\) in the orbit-invariant family.

## Verification

The standalone program `verify_hamming2.py` performs exact rational checks of all displayed formulas and all nontrivial eigenvalues for \(2\le d\le36\), \(2\le q\le32\). It additionally solves the three-variable SLEM linear program independently for a broad selection of dimensions and alphabets, and constructs entire transition matrices for tractable small cases. Run `python verify_hamming2.py` after installing optional packages from `requirements.txt`; the exact rational portion uses only the Python standard library. A completed local execution passed 5,172 assertions. Finite tests corroborate the infinite-family proof rather than replacing it.

## Relationship to prior work

Boyd, Diaconis, and Xiao formulated symmetric fastest-mixing Markov chains as a convex spectral-norm/semidefinite problem. Boyd, Diaconis, Parrilo, and Xiao proved the automorphism-averaging principle and solved the **ordinary distance-one** Hamming graph, among other edge-transitive and distance-transitive families. The present object permits a separate probability for distance-two edges, and the spectral polynomial is genuinely quadratic; the distance-one result alone does not determine its optimum, the two successive three-coordinate alphabet transitions, or the factor-two improvement. Classical Hamming association-scheme methods provide the distance-adjacency eigenvalues, but those spectral formulas alone do not settle the constrained minimax allocation.

Karlin, Lindqvist, and Yao (1993) study random walks on hypercube graphs defined by Hamming-distance cutoffs, making their paper particularly relevant. Its accessible abstract discusses prescribed random-walk spectra and spectral majorization, not an optimization over independently selectable edge weights. The full paper was not accessible for comparison; possible equivalent coverage in it remains a genuine risk.

## Limitations

The classification concerns symmetric stochastic kernels and the absolute nontrivial eigenvalue criterion, not nonreversible kernels, detailed finite-time total-variation optimality, or models in which traversing a distance-two edge costs more than traversing a distance-one edge. The formulas give a globally optimal invariant kernel but do **not** claim that every unrestricted optimizer is invariant. Exact arithmetic computations cover finitely many \((d,q)\); generality is supplied by proof. The novelty comparison is necessarily limited by the inaccessible full text of a plausible historical paper and any unindexed equivalent specialization.

## References

1. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first public preprint 2007-09-06, especially Sections 2–3, https://arxiv.org/abs/0709.0955.
2. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264.
3. S. Karlin, B. Lindqvist, Y.-C. Yao, *Markov Chains on Hypercubes: Spectral Representations and Several Majorization Relations*, Random Structures & Algorithms 4 (1993), 1–36, https://doi.org/10.1002/rsa.3240040102 (bibliographic record and abstract inspected; full text unavailable).
