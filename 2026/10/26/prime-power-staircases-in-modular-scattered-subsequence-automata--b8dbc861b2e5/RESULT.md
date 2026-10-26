# Prime-power staircases in modular scattered-subsequence automata

## Finding

For every prime \(p\), integer \(r\ge2\), and residue \(c\in\mathbb F_p\), write
\[
L_{p,r,c}=\left\{w\in\{0,1\}^{*}:\binom{w}{0^r1}\equiv c\pmod p\right\},
\]
where \(\binom{w}{v}\) counts index-set embeddings of \(v\) as a scattered subsequence of \(w\). Let \(d\ge1\) be uniquely determined by \(p^{d-1}\le r<p^d\). Then the minimal **complete** deterministic finite automaton for \(L_{p,r,c}\) has exactly
\[
\operatorname{sc}(L_{p,r,c})=p^{d+1}=p^{2+\lfloor\log_p r\rfloor}.
\]
The result holds uniformly for all acceptance residues. The state count stays constant on each prime-power block of values of \(r\) and multiplies by \(p\) when \(r\) passes a positive power of \(p\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The word \(0^r1\) is a **scattered** pattern, not a contiguous factor; multiplicities of different index sets are counted. The modulus \(p\) is prime. The stated new all-parameter theorem is restricted to \(r\ge2\); the basic case \(r=1,p=2\) already has a four-state example in Renard–Rigo–Whiteland. No assertion is made for composite moduli or arbitrary patterns. All automata are complete; the empty word is admitted exactly when \(c=0\).

Put \(q=p^d\) and \(f(n)=\binom{n}{r}\bmod p\), for \(n\ge0\). The notation \(\binom{a}{r}\) in the automaton below means the ordinary integer binomial coefficient for the canonical representative \(0\le a<q\), then reduction modulo \(p\).

## Proof

**1. Lucas-periodic upper bound.** By Lucas's theorem, \(f(n)\) is determined by the first \(d\) base-\(p\) digits of \(n\), because \(r<q\). Thus \(f(n+q)=f(n)\) for every \(n\ge0\). For a prefix \(w\), let \(n(w)\) be its number of zeros and \(t(w)=\binom{w}{0^r1}\bmod p\). Appending a zero increases \(n\) by one and does not change \(t\). Appending a one adds \(\binom{n(w)}{r}\), since the new final one can complete precisely that many copies of \(0^r\) selected among existing zeros. Hence the pair \((n(w)\bmod q,t(w))\) is a sufficient deterministic state. Its transitions are
\[
\delta_0(a,t)=(a+1\bmod q,t),\qquad
\delta_1(a,t)=(a,t+f(a)\bmod p).
\]
The initial state is \((0,0)\) and the accepting states satisfy \(t=c\). This gives a complete \(pq\)-state DFA. Both letters act as permutations; the inverse of the one-transition subtracts \(f(a)\).

**2. Reachability.** Fix any \(a\in\{0,\ldots,q-1\}\) and \(t\in\{0,\ldots,p-1\}\). Choose \(N\ge r\) with \(N\equiv a\pmod q\). The word \(0^r1^t0^{N-r}\) reaches \((a,t)\): there are precisely \(t\) contributions, each equal to \(\binom{r}{r}=1\), and no contribution from the final zeros. Consequently all \(pq\) states are reachable.

**3. No translational symmetry in the support of Lucas coefficients.** Define the support
\[
S=\{j\in\mathbb Z/q\mathbb Z:f(j)\ne0\}.
\]
It is well-defined by the period established above. This subset has trivial translation stabilizer. Indeed, if it were invariant under a nonzero translation, its stabilizer, as a nontrivial subgroup of the cyclic group of prime-power order \(q\), would contain \(p^{d-1}=q/p\). But \(r\in S\) because \(f(r)=1\), whereas \(r-q/p\notin S\). To see the latter, the top nonzero base-\(p\) digit of \(r\) lies in position \(d-1\); subtracting \(p^{d-1}\) decreases that digit while leaving the others unchanged, so Lucas's theorem gives \(\binom{r-q/p}{r}\equiv0\pmod p\). Since \(r\ge q/p\), the integer is nonnegative. This contradiction proves the claim about \(S\).

**4. All reachable states have distinct right languages.** Fix any state \((a,t)\) and choose a vector \(\mathbf{k}=(k_0,\ldots,k_{q-1})\in\mathbb F_p^q\), using representatives \(0\le k_j<p\). Form the suffix
\[
z(\mathbf{k})=1^{k_0}0\,1^{k_1}0\cdots0\,1^{k_{q-1}}.
\]
It introduces \(j\) new zeros before block \(1^{k_j}\). Thus the total number of the target subsequence, modulo \(p\), after appending this suffix is
\[
t+\sum_{j=0}^{q-1}k_j f(a+j).
\]
So the set of suffix vectors accepted from \((a,t)\) is the affine hyperplane
\[
H_{a,t}=\left\{\mathbf{k}\in\mathbb F_p^q: \sum_{j=0}^{q-1}k_j f(a+j)=c-t\right\}.
\]
The coefficient vector \(v_a=(f(a),\ldots,f(a+q-1))\) is nonzero: a full period contains \(f(r)=1\). If states \((a,t)\) and \((b,s)\) have identical right languages, they agree on every \(z(\mathbf{k})\), so \(H_{a,t}=H_{b,s}\). Over the field \(\mathbb F_p\), two nontrivial affine linear equations have the same solution set only if the full equations are nonzero scalar multiples. Consequently \(v_b=\lambda v_a\) and \(c-s=\lambda(c-t)\) for some \(\lambda\in\mathbb F_p^{\times}\). In particular \(v_a\) and \(v_b\) have the same support, so \(S+(b-a)=S\). Step 3 forces \(a=b\) modulo \(q\). Then \(v_b=v_a\ne0\), hence \(\lambda=1\), and consequently \(s=t\). Thus all \(pq\) reachable states are Myhill–Nerode inequivalent. The upper bound is exact for every residue \(c\).

## Verification

A dependency-free verifier in `verify.py` reconstructs the automata, performs independent partition-refinement minimization for all accepting residues, compares streaming states against direct integer scattered-embedding counts on 85,995 binary inputs, and tests the support obstruction over additional prime-power periods. Running `python verify.py` prints `VERIFY_OK minimal_automata 44 direct_words 85995`. The 44 counts refer to distinct pairs of parameters; each accepting residue was checked separately. These bounded tests corroborate but do not replace the uniform argument in the preceding section.

## Relationship to prior work

Renard, Rigo, and Whiteland's *Introducing q-deformed binomial coefficients of words* (first posted 2024-02-08, arXiv:2402.05838) proves general recognition of prime-modular scattered-subsequence conditions by permutation automata and explicitly depicts the \(p=2\), pattern \(01\), four-state minimal case (Section 6.2, Figure 4). Its general group-language theorem does **not** give the exact state count for the family \(0^r1\) with \(r\ge2\), nor the prime-power staircase. The same authors' *q-Parikh Matrices and q-deformed binomial coefficients of words* (first posted 2024-02-08, arXiv:2402.05657) develops the underlying polynomial subword statistics and matrix framework but does not give this exact minimal-DFA count. The first paper's general result and the classical Eilenberg characterization are broader in *recognizability*, not stronger in this state-complexity invariant. Here Lucas-periodic compression and a translation-rigid affine-hyperplane separator provide the sharp lower bound.

## Limitations

This theorem does not determine the syntactic group order, the minimum number of transitions in other automaton models, or the complexity for composite moduli or arbitrary mixed-letter subsequence patterns. The argument uses primality both for Lucas's theorem and for the hyperplane scalar-multiple principle. The literary originality comparison is limited to the specifically inspected papers, associated source searches, and the available indexed research; an unindexed special-case theorem might still exist. Computational checks cover finite parameters only. Independent validation has not been performed.

## References

1. A. Renard, M. Rigo, M. A. Whiteland, *Introducing q-deformed binomial coefficients of words*, arXiv:2402.05838v1 (2024-02-08), especially Section 6.2 and Figure 4, https://arxiv.org/abs/2402.05838.
2. A. Renard, M. Rigo, M. A. Whiteland, *q-Parikh Matrices and q-deformed binomial coefficients of words*, arXiv:2402.05657v1 (2024-02-08), especially Sections 1–2, https://arxiv.org/abs/2402.05657.
3. A. Renard, *q-deformed binomial coefficients of words*, public presentation (2024-09-03), prime-group slides, https://orbi.uliege.be/bitstream/2268/322138/1/Journ%C3%A9es_Montoises_2024__Nice_.pdf.
4. É. Lucas, *Théorie des fonctions numériques simplement périodiques* (1878), classical Lucas congruence for binomial coefficients.
