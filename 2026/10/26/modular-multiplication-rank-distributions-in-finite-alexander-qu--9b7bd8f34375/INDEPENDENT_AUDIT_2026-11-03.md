# Independent mathematical audit

## correctness

PASS

With R=F_q[A], the canonical basis operation transports to u*v=α(u)β(v), α automorphism and β:R→S=F_q[H] a surjective linear map of kernel dimension N−h. Choosing H-coset representatives gives R≅S^k, hence the bilinear map ((a_i),(z,w))↦(a_i z)_i. With H=C_(p^a)×B and p∤|B|, each Frobenius orbit O yields S_O=F_(q^d)[T]/(T^m), d=|O|, m=p^a. A local tuple a has left rank t iff its minimum T-adic valuation is m−t; precisely Q^(kt)−Q^(k(t−1)) tuples have that rank (Q=q^d), with one rank-zero tuple. A fixed local z has right rank kt with (Q−1)Q^(t−1) choices and the β-kernel contributes q^(N−h) distinct inputs. For zero products a_i z=0, z=0 gives Q^(km) tuples and valuation ν(z)=m−t gives (Q−1)Q^(t−1+k(m−t)); product over O and the β-fiber gives the proposed Z. The counts and K-ranks each scale by d, so the left/right polynomials and Z are exactly those in RESULT.md. Independent exact prime-field coefficient-space construction (not importing verify.py) enumerated EVERY u and row-reduced the corresponding multiplication matrices for C3/F3, C4/F2, C6/F3 and C12/F2, including rank 0 and zero factors; it reproduced left/right distributions and Z=81,88,26001,444928. A separately calculated Git-tree object SHA1 for the seven read blobs equals the assigned da2607083d5ecb6c984b54e3595c7ad444da5485. Infinite family is proved by the local ring argument, not by exhaustive small examples. Noncyclic p-primary H and nonabelian A remain outside scope.

## originality

PASS

Best-of-knowledge novelty is restricted to the explicit joint three-part quantitative census of individual left and right multiplication ranks and ordered zero-product pairs over every finite Alexander quandle with nontrivial cyclic p-Sylow displacement subgroup, including non-Latin fibers and nonsplit residue fields. Zhang 2026 Proposition 2.1 already supplies the universal transported product and is not novel; the coset free-module observation and local chain-ring decomposition are standard mathematical inputs. Direct inspection of Zhang 2026 (Prop.2.1, Thms 2.2,2.3,5.5), Elhamdadi–Ta–Virgin 2026 (Secs.3–6), Ta 2026 (Thm.4.3, Sec.5) and Churchill et al. 2026 (Sec.6) found related idempotent, integral-domain zero-divisor existence and extended-ring graph results but no explicit rank polynomials or all-input zero-pair count. Three fresh Resultary searches were carried out; their closest graph/invariant records do not imply this distribution. This is not a priority guarantee: equivalent exact valuation enumerators may appear under general finite-chain-ring terminology.

## value

PASS

For the natural nonassociative algebra attached to a finite Alexander quandle, the two entire multiplication-map rank distributions measure all left/right annihilator dimensions; Z is its ordered zero-product incidence statistic. Exactly identifying them for all field sizes and arbitrary cyclic modular Sylow length, with nonsplit Frobenius factors and k>1 non-Latin fibers, supplies a reusable complete classification beyond single finite tables or existence arguments. The modular chain length creates intermediate rank strata unseen in semisimple cases. This is a mathematically motivated invariant and could inform zero-divisor graph and module-structure studies. The value does not rest merely on code reproducibility, or pretend the standard group-ring identity is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
