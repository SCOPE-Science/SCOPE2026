# Bias-robust modular laws for distinct subsequences of independent binary words

## Finding

The number of distinct scattered subsequences of a binary source has an arithmetic residue distribution that is unaffected by *any* boundedly nondegenerate schedule of independent letter probabilities, even if the probabilities change at every position. The uniformity is over all such schedules, not merely over a fixed biased Bernoulli source.

**Theorem.** Fix an integer \(m\ge2\) and \(0<\delta\le1/2\). Let \(B_1,B_2,\ldots\) be independent binary-valued random variables, with \(\delta\le\Pr(B_i=1)\le1-\delta\) for every \(i\). Let \(D_n\) count the *distinct nonempty* subsequence strings of \(W_n=B_1\cdots B_n\); distinct embeddings of the same string are counted only once. Define
\[
 d_m=m^2\prod_{p\mid m}(1-p^{-2}),\qquad K_m=2(d_m-1),\qquad
 \mu_m(r)=\frac{\prod_{p\mid\gcd(m,r+2)}(1-p^{-1})}{m\prod_{p\mid m}(1-p^{-2})}.
\]
Then, for every integer \(n\ge0\) and every residue \(r\),
\[
 \left|\Pr(D_n\equiv r\pmod m)-\mu_m(r)\right|
 \le\left(1-d_m\delta^{K_m}\right)^{\lfloor n/K_m\rfloor}.
\]
In fact, the same right-hand side bounds the total variation distance between a natural two-coordinate subsequence-count state modulo \(m\) and uniform measure on all primitive residue pairs.

For illustration, when \(m=6\), the limiting probabilities in residues \(0,1,2,3,4,5\) are respectively
\[
 (3,4,3,6,2,6)/24.
\]
For a prime modulus \(\ell\), the distinguished residue \(-2\) has limiting probability \(1/(\ell+1)\), and each other residue has limiting probability \(\ell/(\ell^2-1)\).

## Assumptions and scope

A subsequence is obtained by deleting zero or more positions without reordering the remaining positions. The empty subsequence is excluded from \(D_n\), but included in an auxiliary state count. The alphabet is the labeled binary alphabet \(\{0,1\}\). The assumptions require **independence**, though not identical laws or any convergence of the source probabilities. The modulus is any fixed integer at least two. The error bound is a valid, potentially very conservative quantitative guarantee; it does not assert an optimal mixing exponent or hold uniformly as the modulus grows. The empty word is permitted at \(n=0\), with \(D_0=0\).

## Proof

**1. Exactly counting each distinct pattern.** For a deterministic binary prefix \(w\), let \(c_0(w)\), respectively \(c_1(w)\), count the distinct nonempty scattered subsequence *strings* ending in \(0\), respectively \(1\). Put \(X(w)=1+c_0(w)\) and \(Y(w)=1+c_1(w)\). At the empty word, \((X,Y)=(1,1)\). Appending a \(0\) to \(w\) creates precisely the strings \(u0\), where \(u\) ranges over every distinct subsequence of \(w\), including empty, and leaves the strings ending in \(1\) unchanged. The number of strings ending in \(0\) thus becomes \(1+c_0+c_1=X+Y-1\), hence \(X\) becomes \(X+Y\). The corresponding update for appending \(1\) is symmetric. Consequently the two letter maps are
\[
 L(X,Y)=(X+Y,Y),\qquad R(X,Y)=(X,X+Y),
\]
and the number sought is \(D(w)=X(w)+Y(w)-2\). Both maps preserve \(\gcd(X,Y)=1\), so the state always has coprime positive coordinates.

**2. The finite primitive state space.** Modulo \(m\), the possible states belong to
\[
 V_m=\{(x,y)\in(\mathbb Z/m\mathbb Z)^2:\gcd(x,y,m)=1\}.
\]
Counting complementary pairs divisible by each prime dividing \(m\) gives \(|V_m|=d_m\). The maps \(L,R\) are invertible modulo \(m\), with determinant one; each therefore permutes \(V_m\).

Every \((x,y)\in V_m\) has a lift to positive coprime integers \((A,B)\): select a positive integer \(B\equiv y\pmod m\); among positive \(A\equiv x\pmod m\), avoid the residue zero modulo every prime dividing \(B\) but not \(m\), using the Chinese remainder theorem. No prime dividing both \(B\) and \(m\) divides \(A\), by the primitive residue assumption. Thus \(\gcd(A,B)=1\). For any positive coprime \((A,B)\), repeated subtraction of the smaller coordinate from the larger eventually reaches \((1,1)\). Reversing these steps expresses \((A,B)\) as the image of \((1,1)\) under a finite word in \(L,R\). Hence every state of \(V_m\) is reachable from \((1,1)\). Because \(L,R\) are permutations on this finite set, each of their inverse actions equals a positive power, so every state can also reach \((1,1)\). The directed transition graph is strongly connected.

The state \(e=(1,0)\pmod m\) belongs to \(V_m\) and has a self-loop under \(L\). From any state to \(e\), and from \(e\) to any other state, there are paths of length at most \(d_m-1\). By inserting \(L\)-loops at \(e\), there is a directed path of *exactly* \(K_m=2(d_m-1)\) steps between every ordered pair of states.

**3. Uniform contraction even for varying biases.** Denote \(p_i=\Pr(B_i=1)\). The one-step transition is \((1-p_i)P_L+p_iP_R\) where the matrices \(P_L,P_R\) are permutation matrices on \(V_m\). Thus every one-step transition is doubly stochastic and preserves uniform measure \(u_m\) on \(V_m\). Each given path of length \(K_m\) through any time block has probability at least \(\delta^{K_m}\). The exact-length connectivity in step 2 shows that *every entry* of each \(K_m\)-block transition is at least \(\delta^{K_m}\). Therefore that matrix contains the common uniform component of total mass
\[
 \varepsilon_m=d_m\delta^{K_m}\in(0,1].
\]
Its remainder is stochastic. The standard elementary coupling/minorization argument gives, for any two probability distributions on \(V_m\), contraction in total variation by at most \(1-\varepsilon_m\) per complete block. Since \(u_m\) is invariant under *every* step, and the initial state is the point mass at \((1,1)\),
\[
 \|\mathcal L((X(W_n),Y(W_n))\bmod m)-u_m\|_{\mathrm{TV}}
 \le (1-\varepsilon_m)^{\lfloor n/K_m\rfloor}.
\]
The proof uses only the common bias lower bound, so it remains valid for an arbitrarily varying deterministic schedule \((p_i)\).

**4. Arithmetic projection.** For a fixed residue \(s\pmod m\), writing \(y=s-x\) shows that \(\gcd(x,y,m)=1\) if and only if \(\gcd(x,s,m)=1\). By inclusion-exclusion, the number of suitable \(x\pmod m\) is
\[
 m\prod_{p\mid\gcd(m,s)}(1-p^{-1}).
\]
Since \(D=X+Y-2\), the event \(D\equiv r\pmod m\) corresponds to \(s=r+2\). Dividing this fiber count by \(d_m\) gives
\[
 \Pr_{u_m}(D\equiv r\pmod m)
 =\frac{\prod_{p\mid\gcd(m,r+2)}(1-p^{-1})}{m\prod_{p\mid m}(1-p^{-2})}.
\]
Total variation cannot increase under a deterministic projection, giving the announced inequality. (The offset accounts for excluding the empty subsequence.)

**5. Why a nondegeneracy condition matters.** If \(p_i=2^{-i-4}\), then \(\sum_{i\ge1}p_i=1/16\). By the union bound, \(\Pr(W_n=0^n)\ge15/16\) for every \(n\). On that event the number of distinct nonempty subsequences is \(n\), so some residue has probability at least \(15/16\) for every \(n\). But the largest mass of the primitive-pair limiting law is at most \(2/3\) for every \(m\ge2\). Convergence to the universal arithmetic law therefore fails for this independent, increasingly degenerate source. This does not claim that the uniform ellipticity condition is logically necessary.

## Verification

A standard-library Python verifier independently constructs the *sets* of distinct scattered subsequences of every binary word of length at most twelve (\(8191\) words). It checks the two-coordinate recurrence, coprimality, primitive-residue graph reachability and the arithmetic fiber formula for moduli \(2\) through \(24\). It also compares an exact weighted finite-state calculation with explicit enumeration of all source words across \(45\) non-identically distributed rational-probability cases, and numerically verifies contraction toward uniform on primitive states for nine moduli and a varying bias schedule. The checks concern finite cases only; the infinite theorem rests on the proof above.

Reproduce with `python verify.py`. No nonstandard packages or external data are needed.

## Relationship to prior work

Reznick established uniform distribution of Stern's consecutive coprime pairs among feasible residue pairs under uniform-level sampling. That result already covers the **fair, identically distributed** binary source and its limiting residue frequencies; those are *not* presented as novel here. Żak identified the relationship between counts of binary subsequences and coprime-pair/continued-fraction recursions. These structural tools motivate and underlie the argument. Biers-Ariel, Godbole and Kelley analyze expectations of distinct subsequence counts for randomly generated binary strings, including a fixed biased Bernoulli source; they do not establish the full modular distribution of the count under arbitrary time-varying biases. Baake and Coons investigate an associated Stern-derived real-valued measure, but not this finite-modulus nonstationary-source statement.

The distinguishing assertion here is the **single uniform quantitative mixing and residue formula for every independent, even nonstationary, elliptic binary source**, together with the source-degeneracy boundary. The finite-state minorization mechanism itself is standard and is not claimed as new. The same conclusion may be a corollary of a broader unlocated random-product theorem; the originality claim is restricted to the explicit source/count/modulus result and its arithmetic identification.

## Limitations

The mixing exponent is deliberately conservative and no optimal spectral gap is claimed. Source independence is essential to the stated proof. The modulo-\(m\) claim does not imply a limiting distribution of the unbounded integer count. No statement of unique novelty is made beyond the literature that could be inspected. An unindexed theorem on arbitrary products of Stern matrices might cover the new statement implicitly.

## References

1. R. Żak, *Finding binary words with a given number of subsequences*, arXiv:2210.00342v1, October 1, 2022, https://arxiv.org/abs/2210.00342 .
2. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601, October 19, 2006, https://arxiv.org/abs/math/0610601 .
3. Y. Biers-Ariel, A. Godbole, E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661, April 27, 2017, https://arxiv.org/abs/1704.08661 .
4. M. Baake, M. Coons, *A natural probability measure derived from Stern's diatomic sequence*, arXiv:1706.00187, 2017, https://arxiv.org/abs/1706.00187 .
