# Independent mathematical audit

## correctness

PASS

Rule 18 local rule is (Phi x)_i=1 exactly on 001 and 100, equivalently (1+x_i)(x_{i−1}+x_{i+1}) over F2. Cyclic summation over any n-periodic input cancels both linear neighbor sums and both quadratic neighbor products, forcing even output weight. If an n-periodic image y contains 11, the unique forced input four-block is 1001 at each occurrence, permitting a cut-and-periodic-splice to construct n-periodic antecedent. If y is cyclic 11-free, the bilateral phase p_{i+1}=p_i xor y_i and x_i=p_i(1−y_i) directly produce Phi x=y, periodic with period n for even weight and 2n for odd. Thus the exact exception set is cyclic 11-free odd-weight words; a primitive output exception forces least antecedent period 2n. The transfer matrix M(t)=[[1,t],[1,0]] counts cyclic 11-free output words by weight, giving E_n=(Lucas_n−2cos(nπ/3))/2, its rational generating function z²(2−z)/((1−z−z²)(1−z+z²)), and asymptotic ~phi^n/2. Independent brute-force finite-ring input images for n=1..8 compared n vs 2n outputs and odd cyclic 11-free exceptions. The proof is bilateral and covers n=1,2 boundary; these finite cases are not an infinite proof.

## originality

PASS

Best-of-knowledge statement-level primary-literature comparison: the identified antecedents cover qualitative mechanisms, methods or partial counts but no inspected theorem implies the precise assessed evaluated claim; limitations and possible older equivalents remain explicit. Same-period preimage existence is the weak periodic point property, and cyclic 11-free words are the golden-mean subshift. The unquantified weakness and local marker parity are prior art; the evaluated all-n exception language, exact Lucas/character count and sharp 2n lift are the assessed statements.

## value

PASS

An exact same-period preimage obstruction language with its all-period Lucas census and sharp period-doubling remedy is a natural dynamical invariant of a canonical elementary cellular automaton. The result refines the qualitative weak periodic-point condition with computable periodic growth and a constructive universal lift. The Lucas enumeration by itself is classical; its exact identification with this obstruction is the mathematically motivated contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
