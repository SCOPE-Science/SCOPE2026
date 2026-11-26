# Independent mathematical audit

## correctness

PASS

VT checksum residues modulo n+1 distinguish any two distinct insertions into a shared read. The integer checksum difference for different insertion bits lies in [1,n] or [-n,-1]; for the same bit it counts the intervening opposite bits up to sign, and zero yields the same word. This gives the clique upper bound. The two small examples work by literal deletion: the one-1 words share the all-zero read, and the extra word shares an end-1 read with each while ruling out the all-zero read. The common-insertion lemma also checks: in a common supersequence, if the coordinate deleted to give u is earlier, it can slide through the constant run to the first index where u and v differ; the inserted symbol and index are then forced. The other order yields at most one other candidate. The base-case sentence describing the lemma has its quantifiers reversed: the needed application is that two distinct reads cannot have three prescribed common parents. Thus any three star words share only u_n. At n=5 the five listed words share the displayed reads with v_5; v_5 does not contain u_5 as a one-deletion read. For induction, insertions into u_nt_n are formerly valid insertions with t_n appended plus the single exceptional insertion u_nt_n(1-t_n). The invariant on v_n persists when the alternating suffix is appended. The new word shares v_n with v_{n+1}; it shares u_nt_n with the appended star members, not with v_{n+1}. Appending t_n preserves the old edges, and the exceptional outsider stays outside the star, so the whole family has size n+1 and empty total intersection. At n=1 or 2 any clique lies in an insertion neighborhood. The proof suffices for all lengths; the finite script was inspected, not run.

## originality

PASS

The supported distinction is attaining the classical n+1 upper bound with no common read at every n>=3, not the bound or the ordinary clique number. The inspected overlaps do not provide the globally incompatible equality family in the one-common-read graph.

## value

PASS

It resolves whether a global read is forced at maximum pairwise ambiguity. There is no penalty in clique size for forbidding a common read, not just a small non-Helly example. The all-length explicit construction is useful for distinguishing a maximum clique from a canonical insertion neighborhood in the binary deletion graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
