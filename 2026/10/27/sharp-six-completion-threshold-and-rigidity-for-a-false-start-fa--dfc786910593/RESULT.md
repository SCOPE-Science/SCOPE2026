# Sharp six-completion threshold and rigidity for a false-start fair duel

## Finding
Let \(\lambda(i)\) be the minimum length of a nonexceptional sign word that admits an \(i\)-completion in the fair-duel construction of Khovanova and Madhavarapu. Then
\[
\lambda(6)=17.
\]
Exactly two nonexceptional sign words of length \(17\) admit a \(6\)-completion: \(T_4T_0\) and its sign complement, where \(T_j\) is the signed Thue–Morse word of length \(2^j\), beginning with \(-1\). Written explicitly, the normalized extremizer is
\[
(-1,+1,+1,-1,+1,-1,-1,+1,+1,-1,-1,+1,-1,+1,+1,-1,-1).
\]
Under the period correspondence established in the source paper, each such word produces a fair-duel continuation of least period \(256\). No shorter nonexceptional prefix achieves that period.

## Assumptions and scope
A sign word is a finite sequence over \(\{-1,+1\}\). It is *exceptional* if it is a prefix of the infinite signed Thue–Morse word or of its sign complement. We adopt the source paper's recursive \(i\)-completion operation, not an arbitrary periodic continuation. Put
\[
F_s(x)=\sum_{k=0}^{|s|-1}s_k(1-x)^k,
\quad c_i(s)=[x^i]F_s(x)=(-1)^i\sum_{k=i}^{|s|-1}\binom{k}{i}s_k.
\]
At completion stage \(i\), write \(b_i=c_i(s^{(i-1)})/2^{i(i-1)/2}\). The stage is admissible precisely when \(b_i\) is an integer; if it is admissible, append \(|b_i|\) copies of \(T_i\) when \(b_i>0\), its sign complement when \(b_i<0\), or no symbols when \(b_i=0\). Stages start at \(i=0\). The target property is admissibility through stage \(6\), inclusive.

## Proof
The coefficient of \(x^i\) in \(F_{T_i}\) is \(-2^{i(i-1)/2}\), while all lower coefficients vanish. Therefore the prescribed stage cancels \(c_i\) without altering previously canceled coefficients. This establishes the stated exact divisibility test.

For every length \(n\) with \(2\le n\le17\), enumerate all \(2^{n-1}\) sign words with first sign \(-1\). Discard the sole exceptional prefix at that orientation. This represents every nonexceptional word up to the symmetry \(s\mapsto-s\), which preserves completion admissibility and exchanges completing blocks with their complements.

To evaluate a prefix without constructing potentially enormous appendices, perform arithmetic in the exact integer polynomial ring \(\mathbb Z[x]/(x^7)\). The signed Thue–Morse block has generating polynomial
\[
F_{T_i}(x)=-\prod_{r=0}^{i-1}\bigl(1-(1-x)^{2^r}\bigr).
\]
When stage \(i\) appends \(k=|b_i|\) copies with sign \(\sigma=\operatorname{sgn}(b_i)\) to a current word of length \(L\), its exact coefficient update through degree six is
\[
\Delta F(x)=\sigma(1-x)^L F_{T_i}(x)
\sum_{t=0}^{k-1}(1-x)^{2^it}\pmod{x^7}.
\]
The final sum is computed by binary doubling of geometric sums. Every arithmetic operation is integral and exact; truncation cannot affect coefficients of degree at most six. The supplied `repro/exhaustive_threshold.py` implements this recurrence and checks every normalized nonexceptional word in the stated finite domain.

The computed number of normalized words admitting a six-completion is zero at each length \(2,3,\ldots,16\), and exactly one at length \(17\). The unique survivor equals \(T_4T_0\), as asserted in the machine-checkable script. A nonexceptional word of length one does not exist, because both one-letter prefixes are exceptional. Thus \(17\) is the minimum length, and sign complementation gives exactly two labeled minimizers. This finite exhaustion is a complete proof for the claimed minimum, rather than a sample-based extrapolation.

## Verification
Run `python3 repro/exhaustive_threshold.py`, which enumerates all normalized candidates and checks exact coefficient updates; its explicit assertions include the minimum, uniqueness, and witness identity. Independently run `python3 repro/direct_witness.py`, which physically appends completing blocks and evaluates binomial coefficient sums for the claimed minimizer. It confirms admissibility through stage six, a completed length of \(960\), and failure of stage seven. The scripts rely only on the Python standard library. They do not claim any infinite general formula for \(\lambda(i)\).

## Relationship to prior work
Khovanova and Madhavarapu, *Fair Duels after a False Start*, arXiv:2610.00880v1 (first public version October 1, 2026), introduced the completion criterion and proved the general upper bound \(\lambda(i)\le2^{i-2}+1\) for \(i\ge2\). Substitution \(i=6\) gives \(\lambda(6)\le17\), but does not prove that shorter nonexceptional prefixes are impossible or classify equality cases. The present exact finite exhaustion establishes both. Their period correspondence identifies the period \(2^{6+2}=256\).

## Limitations
The proof is confined to the sixth completion stage and minimum-length prefixes; it does not settle the general growth of \(\lambda(i)\). The finite exhaustive program and the direct witness checker use different representations but are not independent external validation. Historical priority cannot exclude equivalent unpublished or unindexed computations.

## References
Khovanova, T., and Madhavarapu, T., *Fair Duels after a False Start*, arXiv:2610.00880v1, October 1, 2026. https://arxiv.org/abs/2610.00880
