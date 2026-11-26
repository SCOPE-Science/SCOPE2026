# Independent mathematical audit

## correctness

PASS

Read the frozen factor-cover proof and eertree implementation. The four states distinguish a leading-zero prefix, an even zero run, an odd run, and a permanently failed internal odd run; accepted states give b_0=1 and the specified digits. The eight pair types all occur already in the four-letter prefix ABCBBDCBCBDDBDCB and are closed under adjacent pairs of substituted words; this proves both directions of the pair inventory. Every length <=8192 factor lies in at most two successive aligned blocks of size 8192, and each pair block occurs. DD supplies 0^n for every n in scope. A new distinct palindrome at a right endpoint must be the longest palindromic suffix (any shorter palindromic suffix also occurs as a prefix of the longest); literal keys deduplicate across blocks without approximation. Independently generated an actual 106496-symbol digit-defined prefix containing representatives of all eight aligned pair types and used Manacher radii, not the uploaded eertree, with literal substring sets for palindromes containing a 1 (/workspace/review_work/baum.py). The full profile agrees at all lengths 1–8192, digest c94eac15fdef31d2b90ccd14121e0782788a316c05a5c80f9d7bde100ff05e55, with 66 exceptional and 8082 zero-only lengths in 45–8192. This certifies nothing about larger lengths.

## originality

PASS

The assessed fact is the complete actual palindrome profile of this word through 8192, not the known automaticity of the word or general regularity of an automatic word's palindromic complexity. No earlier exact table or equivalent Baum–Sweet-specific representation covering the range was found in the inspected sources.

## value

PASS

Palindromic complexity is a standard exact language invariant, tested here on the classical nonprimitive Baum–Sweet word. The dyadic cutoff uses the natural substitution scale and resolves several scales of two different parity bands, including the earliest irregular lengths and the complete complement, not a prefix-occurrence sample or isolated hand-computable values. The profile is a useful finite benchmark and potential structural clue, without inferring an infinite pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
